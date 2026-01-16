from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.platypus import (
    SimpleDocTemplate,
    Paragraph,
    Table,
    TableStyle,
    Spacer,
    HRFlowable,
)
from reportlab.lib import colors


def export_to_pdf(df, filename="data/llm_results_report.pdf"):
    doc = SimpleDocTemplate(
        filename,
        pagesize=A4,
        rightMargin=36,
        leftMargin=36,
        topMargin=36,
        bottomMargin=36,
    )

    styles = getSampleStyleSheet()
    elements = []

    # ===== Title =====
    elements.append(Paragraph("LLM Evaluation Report", styles["Title"]))
    center_style = styles["Normal"].clone("center_style")
    center_style.alignment = 1  # 1 = CENTER

    elements.append(
        Paragraph(
            "Evaluation of a rule-based system supported by LLM judgment",
            center_style,
        )
    )


    elements.append(Spacer(1, 8))
    elements.append(HRFlowable(width="100%", thickness=1, color=colors.darkblue))
    elements.append(Spacer(1, 16))

    # ===== Introduction =====
    intro_text = """
    This report presents the evaluation of a rule-based system designed to detect
    logical inconsistencies in textual context.
    The system is tested using predefined test cases and its decisions are further
    reviewed by a Large Language Model acting as an independent judge.
    The goal of this evaluation is to identify weaknesses of deterministic rules and
    demonstrate how LLM-based judgment can support quality assurance in AI systems.
    """

    elements.append(Paragraph("<b>Introduction</b>", styles["Heading2"]))
    elements.append(Spacer(1, 6))
    elements.append(Paragraph(intro_text, styles["Normal"]))
    elements.append(Spacer(1, 18))

    # ===== Summary =====
    total_tests = len(df)
    errors_df = df[df["result"] != df["expected"]]
    error_rate = round(len(errors_df) / total_tests, 2)

    false_positives = len(
        df[(df["result"] == "FAIL") & (df["expected"] == "PASS")]
    )
    false_negatives = len(
        df[(df["result"] == "PASS") & (df["expected"] == "FAIL")]
    )

    elements.append(Paragraph("<b>Evaluation Summary</b>", styles["Heading2"]))
    elements.append(Spacer(1, 6))
    elements.append(Paragraph(f"Number of test cases: {total_tests}", styles["Normal"]))
    elements.append(Paragraph(f"Error rate: {error_rate}", styles["Normal"]))
    elements.append(Paragraph("Risky types: context_conflict", styles["Normal"]))
    elements.append(Paragraph(f"False positives: {false_positives}", styles["Normal"]))
    elements.append(Paragraph(f"False negatives: {false_negatives}", styles["Normal"]))
    elements.append(Spacer(1, 18))

    # ===== Table styles =====
    table_text_style = styles["Normal"].clone("table_text")
    table_text_style.fontSize = 9

    header_style = styles["Normal"].clone("header_style")
    header_style.fontSize = 9
    header_style.fontName = "Helvetica-Bold"

    # ===== Table =====
    table_data = [
        [
            Paragraph("Test ID", header_style),
            Paragraph("Result", header_style),
            Paragraph("Expected", header_style),
            Paragraph("Test type", header_style),
            Paragraph("LLM agrees", header_style),
            Paragraph("LLM comment", header_style),
        ]
    ]

    for _, row in df.iterrows():
        table_data.append(
            [
                Paragraph(str(row["test_id"]), table_text_style),
                Paragraph(str(row["result"]), table_text_style),
                Paragraph(str(row["expected"]), table_text_style),
                Paragraph(str(row["test_type"]), table_text_style),
                Paragraph(str(row["llm_agrees"]), table_text_style),
                Paragraph(str(row["llm_comment"]), table_text_style),
            ]
        )

    table = Table(
        table_data,
        colWidths=[55, 45, 55, 90, 60, 185],
        repeatRows=1,
    )

    table.setStyle(
        TableStyle(
            [
                ("BACKGROUND", (0, 0), (-1, 0), colors.whitesmoke),
                ("GRID", (0, 0), (-1, -1), 0.25, colors.grey),
                ("VALIGN", (0, 0), (-1, -1), "TOP"),
                ("LEFTPADDING", (0, 0), (-1, -1), 6),
                ("RIGHTPADDING", (0, 0), (-1, -1), 6),
                ("TOPPADDING", (0, 0), (-1, -1), 4),
                ("BOTTOMPADDING", (0, 0), (-1, -1), 4),
            ]
        )
    )

    elements.append(table)
    elements.append(Spacer(1, 24))

    # ===== Footer =====
    footer_style = styles["Normal"].clone("footer")
    footer_style.fontSize = 8
    footer_style.textColor = colors.grey

    elements.append(
        Paragraph(
            "Generated automatically as part of an AI quality assurance pipeline.",
            footer_style,
        )
    )

    # ===== Build PDF =====
    doc.build(elements)
    print("PDF saved as:", filename)
