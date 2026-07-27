#!/usr/bin/env python3
"""Generate PDF for the academic CV (content mirrors cv.html)."""

from pathlib import Path

from reportlab.lib.colors import HexColor
from reportlab.lib.enums import TA_CENTER, TA_RIGHT
from reportlab.lib.pagesizes import letter
from reportlab.lib.styles import ParagraphStyle, getSampleStyleSheet
from reportlab.lib.units import inch
from reportlab.platypus import (
    Flowable,
    HRFlowable,
    KeepTogether,
    PageBreak,
    Paragraph,
    SimpleDocTemplate,
    Spacer,
)

ROOT = Path(__file__).resolve().parent.parent
PDF_PATH = ROOT / "Md_Ashikur_Rahman_Academic_CV.pdf"

NAVY = HexColor("#00274c")
MUTED = HexColor("#5f6b75")
LINE = HexColor("#c5cdd3")
BODY = HexColor("#222222")

LOCATION_LINE = "Dhaka, Bangladesh"

CONTACT_PARTS = [
    ("link", "mdashikur.rafi@gmail.com", "mailto:mdashikur.rafi@gmail.com"),
    ("text", " · "),
    ("text", "+880 1675 964 080"),
    ("text", " · "),
    ("link", "Homepage", "https://ashikrafi.github.io/"),
    ("text", " · "),
    ("link", "Google Scholar", "https://scholar.google.com/citations?user=Htgw_vEAAAAJ&hl=en"),
    ("text", " · "),
    ("link", "GitHub", "https://github.com/ashikrafi"),
    ("text", " · "),
    ("link", "LinkedIn", "https://www.linkedin.com/in/mdashikrah/"),
]

RESEARCH_INTERESTS = (
    "Trustworthy multimodal machine learning; vision-language models; AI safety and robustness."
)

PEER_REVIEWED = [
    "[P1] Abdullah Ibne Hanif Arean, Niamul Hassan Samin, Md Arifur Rahman, Renu Akter Sweety, "
    "Juena Ahmed Noshin, <b>Md Ashikur Rahman</b>*. "
    "&ldquo;Stroke-Level Connectivity Verification: Grounding Vision-Language Models Against "
    "Topology Hallucination in Diagram Understanding.&rdquo; "
    "<i>International Conference on Document Analysis and Recognition (ICDAR)</i>, 2026. "
    "Accepted for oral presentation. *Corresponding author. "
    '<link href="https://github.com/tkcl-research/LogicBench1k" color="#00274c"><u>[Code]</u></link>',
]

UNDER_REVIEW = [
    "[M1] <b>Md Ashikur Rahman</b>, Md Arifur Rahman, Niamul Hassan Samin, Khandaker Rifah Tasnia, "
    "Sifat Rahman Ahona, Juena Ahmed Noshin. "
    "&ldquo;Beyond Aggregate Risk: Role-Stratified Conformal Risk Control for LLM Tool Calls.&rdquo; "
    "Manuscript under review, 2026.",
    "[M2] <b>Md Ashikur Rahman</b>, Juena Ahmed Noshin, Niamul Hassan Samin, Abdullah Ibne Hanif Arean, "
    "Md Hasibul Amin, Md Arifur Rahman. "
    "&ldquo;When Detector-Based Grounding Metrics Measure Vocabulary: A Cautionary Audit of Entity "
    "Claims in Video-QA Reasoning Traces.&rdquo; "
    "Manuscript under review, 2026.",
    "[M3] <b>Md Ashikur Rahman</b>, Md Arifur Rahman, Nusrat Jahan Trisna, Juena Ahmed Noshin. "
    "&ldquo;Math-Encoded Jailbreaks Across Provider-Matched Models and Inference-Time Reasoning "
    "Configurations.&rdquo; "
    "Manuscript under review, 2026.",
]

ADDITIONAL_PUBLICATION = [
    "[A1] &ldquo;Automated Detection of Diabetic Retinopathy Using Deep Residual Learning.&rdquo; "
    "<i>International Journal of Computer Applications</i>, 2020.",
]


def _escape(text: str) -> str:
    return text.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")


def build_styles():
    styles = getSampleStyleSheet()
    styles.add(
        ParagraphStyle(
            name="ResumeName",
            fontName="Helvetica-Bold",
            fontSize=15,
            leading=18,
            alignment=TA_CENTER,
            textColor=NAVY,
            spaceAfter=2,
        )
    )
    styles.add(
        ParagraphStyle(
            name="ResumeContact",
            fontName="Helvetica",
            fontSize=8,
            leading=10.5,
            alignment=TA_CENTER,
            textColor=NAVY,
            spaceAfter=3,
        )
    )
    styles.add(
        ParagraphStyle(
            name="SectionTitle",
            fontName="Helvetica-Bold",
            fontSize=9.5,
            leading=12,
            textColor=NAVY,
            spaceBefore=7,
            spaceAfter=2,
            leftIndent=0,
            firstLineIndent=0,
        )
    )
    styles.add(
        ParagraphStyle(
            name="EntryTitle",
            fontName="Helvetica-Bold",
            fontSize=9,
            leading=11,
            textColor=NAVY,
            leftIndent=0,
            firstLineIndent=0,
        )
    )
    styles.add(
        ParagraphStyle(
            name="EntryDates",
            fontName="Helvetica",
            fontSize=8.5,
            leading=11,
            alignment=TA_RIGHT,
            textColor=MUTED,
        )
    )
    styles.add(
        ParagraphStyle(
            name="Subhead",
            fontName="Helvetica-Oblique",
            fontSize=8.5,
            leading=11,
            textColor=BODY,
            spaceBefore=3,
            spaceAfter=1,
        )
    )
    styles.add(
        ParagraphStyle(
            name="ResumeBullet",
            fontName="Helvetica",
            fontSize=8.5,
            leading=10.5,
            textColor=BODY,
            leftIndent=10,
            bulletIndent=0,
            spaceAfter=0.5,
        )
    )
    styles.add(
        ParagraphStyle(
            name="Degree",
            fontName="Helvetica-Bold",
            fontSize=9,
            leading=11,
            textColor=NAVY,
            spaceAfter=1,
        )
    )
    styles.add(
        ParagraphStyle(
            name="Summary",
            fontName="Helvetica",
            fontSize=8.5,
            leading=10.5,
            textColor=BODY,
            spaceAfter=1,
            leftIndent=0,
            firstLineIndent=0,
        )
    )
    styles.add(
        ParagraphStyle(
            name="PubItem",
            fontName="Helvetica",
            fontSize=8.5,
            leading=10.5,
            textColor=BODY,
            leftIndent=0,
            firstLineIndent=0,
            spaceAfter=3,
        )
    )
    styles.add(
        ParagraphStyle(
            name="SkillLine",
            fontName="Helvetica",
            fontSize=8.5,
            leading=10.5,
            textColor=BODY,
            spaceAfter=1.5,
        )
    )
    return styles


class EntryHeader(Flowable):
    """Title at frame left edge; date right-aligned on the same line (no Table overhang)."""

    def __init__(self, title: str, dates: str, styles, date_width=1.55 * inch):
        Flowable.__init__(self)
        self._title = Paragraph(_escape(title), styles["EntryTitle"])
        self._dates = Paragraph(_escape(dates), styles["EntryDates"]) if dates else None
        self._date_width = date_width
        self._title_h = 0
        self._dates_h = 0

    def wrap(self, availWidth, availHeight):
        self.width = availWidth
        gap = 6 if self._dates else 0
        title_w = availWidth - (self._date_width + gap if self._dates else 0)
        _, self._title_h = self._title.wrap(title_w, availHeight)
        self._dates_h = 0
        if self._dates:
            _, self._dates_h = self._dates.wrap(self._date_width, availHeight)
        self.height = max(self._title_h, self._dates_h) + 1
        return self.width, self.height

    def draw(self):
        y_title = self.height - self._title_h
        self._title.drawOn(self.canv, 0, y_title)
        if self._dates:
            y_dates = self.height - self._dates_h
            self._dates.drawOn(self.canv, self.width - self._date_width, y_dates)


def entry_header_table(title: str, dates: str, styles) -> Flowable:
    return EntryHeader(title, dates, styles)


def bullets(items, styles):
    return [Paragraph(f"• {_escape(item)}", styles["ResumeBullet"]) for item in items]


def section_rule():
    return HRFlowable(width="100%", thickness=0.8, color=LINE, spaceBefore=0, spaceAfter=3)


def contact_pdf_html():
    parts = []
    for item in CONTACT_PARTS:
        if item[0] == "text":
            parts.append(_escape(item[1]))
        else:
            parts.append(
                f'<link href="{item[2]}" color="#00274c"><u>{_escape(item[1])}</u></link>'
            )
    return "".join(parts)


def role_block(title, dates, items, styles):
    block = [entry_header_table(title, dates, styles)]
    block.extend(bullets(items, styles))
    block.append(Spacer(1, 3))
    return KeepTogether(block)


def build_pdf():
    styles = build_styles()
    doc = SimpleDocTemplate(
        str(PDF_PATH),
        pagesize=letter,
        leftMargin=0.55 * inch,
        rightMargin=0.55 * inch,
        topMargin=0.45 * inch,
        bottomMargin=0.45 * inch,
        title="Md Ashikur Rahman | Academic CV",
        author="Md Ashikur Rahman",
    )

    story = []
    story.append(Paragraph("Md Ashikur Rahman", styles["ResumeName"]))
    story.append(Paragraph(_escape(LOCATION_LINE), styles["ResumeContact"]))
    story.append(Paragraph(contact_pdf_html(), styles["ResumeContact"]))

    story.append(Paragraph("RESEARCH INTERESTS", styles["SectionTitle"]))
    story.append(section_rule())
    story.append(Paragraph(_escape(RESEARCH_INTERESTS), styles["Summary"]))

    story.append(Paragraph("EDUCATION", styles["SectionTitle"]))
    story.append(section_rule())
    story.append(
        entry_header_table(
            "American International University-Bangladesh", "2011 - 2015", styles
        )
    )
    story.append(Paragraph("B.Sc. in Computer Science and Engineering", styles["Degree"]))
    story.extend(
        [
            Paragraph(
                "• CGPA: 3.87/4.00; top 3%; <i>magna cum laude</i>",
                styles["ResumeBullet"],
            ),
            Paragraph(
                "• Merit Scholarship and Tuition Fee Waiver",
                styles["ResumeBullet"],
            ),
        ]
    )

    story.append(Paragraph("PEER-REVIEWED PUBLICATIONS", styles["SectionTitle"]))
    story.append(section_rule())
    for pub in PEER_REVIEWED:
        story.append(Paragraph(pub, styles["PubItem"]))

    story.append(Paragraph("PREPRINTS AND MANUSCRIPTS UNDER REVIEW", styles["SectionTitle"]))
    story.append(section_rule())
    for item in UNDER_REVIEW:
        story.append(Paragraph(item, styles["PubItem"]))

    story.append(Paragraph("ADDITIONAL PUBLICATION", styles["SectionTitle"]))
    story.append(section_rule())
    for pub in ADDITIONAL_PUBLICATION:
        story.append(Paragraph(pub, styles["PubItem"]))

    story.append(Paragraph("PROFESSIONAL EXPERIENCE", styles["SectionTitle"]))
    story.append(section_rule())
    story.append(
        entry_header_table(
            "Lead AI Engineer, The KOW Company", "Jan 2023 - Present", styles
        )
    )
    story.append(Paragraph("Research", styles["Subhead"]))
    story.extend(
        bullets(
            [
                "Lead applied research on AI safety, multimodal reliability, vision-language grounding and hallucination, uncertainty estimation, and risk-controlled LLM tool use.",
                "Designed a role-stratified conformal risk-control framework for heterogeneous LLM tool calls [M1].",
                "Conducted a cautionary audit of detector-based grounding metrics on video question-answering reasoning traces [M2].",
                "Designed evaluations of math-encoded jailbreaks across provider-matched models and inference-time reasoning configurations [M3].",
                "Developed stroke-level connectivity verification for topology hallucination in diagram understanding; last and corresponding author on an ICDAR 2026 oral paper [P1].",
                "Develop evaluation frameworks, benchmarks, and reproducible pipelines for multimodal grounding, hallucination analysis, and model reliability.",
            ],
            styles,
        )
    )
    story.append(Paragraph("Engineering Leadership", styles["Subhead"]))
    story.extend(
        bullets(
            [
                "Lead a multidisciplinary engineering team building and deploying multimodal AI products spanning image generation, virtual try-on, computer vision, and 3D reconstruction (Retouched.ai, Omnimage.ai, HoloSnap.ai, CogniX, and The Fitting Room).",
                "Provide technical leadership across machine-learning architecture, code review, offline evaluation, production deployment, and cross-functional delivery.",
            ],
            styles,
        )
    )

    story.append(Paragraph("RESEARCH MENTORING", styles["SectionTitle"]))
    story.append(section_rule())
    story.extend(
        bullets(
            [
                "Mentor and supervise four researchers on literature review, research planning, experimental design, reproducible implementation, result analysis, and academic writing.",
                "Advise junior collaborators through manuscript preparation and submission on projects in vision-language grounding, LLM safety, and risk-controlled tool use.",
            ],
            styles,
        )
    )

    story.append(Paragraph("RESEARCH ARTIFACTS", styles["SectionTitle"]))
    story.append(section_rule())
    story.append(
        Paragraph(
            '• <b><link href="https://github.com/tkcl-research/LogicBench1k" color="#00274c">'
            "<u>LogicBench-1K</u></link></b>: Diagram benchmark and supporting artifacts for "
            "evaluating topology hallucination and structural grounding; released with the "
            "ICDAR 2026 paper [P1]. Role: research lead and corresponding author; contributions "
            "include problem formulation, benchmark design oversight, evaluation methodology, "
            "and manuscript leadership.",
            styles["ResumeBullet"],
        )
    )

    story.append(PageBreak())
    story.append(Paragraph("PRIOR EXPERIENCE", styles["SectionTitle"]))
    story.append(section_rule())
    story.append(
        role_block(
            "Senior Machine Learning Engineer, The KOW Company",
            "Jul 2021 - Dec 2022",
            [
                "Improved object-detection and segmentation performance by 20-35% on internal benchmarks; resulting models were deployed through Retouched.ai.",
                "Led more than six client machine-learning engagements and built offline evaluation and production A/B testing workflows for model quality and reliability.",
            ],
            styles,
        )
    )
    story.append(
        role_block(
            "Machine Learning Engineer, The KOW Company",
            "Jul 2020 - Jun 2021",
            [
                "Developed production deep-learning models and scalable training and evaluation pipelines for object recognition, segmentation, and background removal.",
            ],
            styles,
        )
    )
    story.append(
        role_block(
            "Senior Software Engineer, Smart Technologies (BD) Ltd.",
            "May 2017 - Dec 2019",
            [
                "Led development of enterprise supply-chain systems, including architecture and optimization of a 4 TB SQL Server deployment; reduced report generation from approximately 20 minutes to under one minute.",
            ],
            styles,
        )
    )
    story.append(
        role_block(
            "Software Engineer, Proggasoft",
            "Mar 2015 - Aug 2016",
            [
                "Developed production web applications and backend systems for DevSkill.com using ASP.NET MVC and SQL.",
            ],
            styles,
        )
    )

    story.append(Paragraph("AWARDS AND INVITED TALKS", styles["SectionTitle"]))
    story.append(section_rule())
    story.extend(
        bullets(
            [
                "Champion, BASIS National ICT Awards, 2020 (Retouched.ai)",
                "Finalist, Asia Pacific ICT Alliance Awards, 2021",
                "Artificial Intelligence in Advertising, invited workshop speaker, Daffodil International University",
            ],
            styles,
        )
    )

    story.append(Paragraph("TECHNICAL SKILLS", styles["SectionTitle"]))
    story.append(section_rule())
    for label, text in [
        (
            "Research Methods:",
            "Experimental design; benchmark and dataset design; ablation studies; error analysis; conformal prediction and risk control; calibration and uncertainty evaluation; grounding and hallucination evaluation",
        ),
        (
            "Multimodal AI:",
            "Vision-language models; visual grounding; multimodal reasoning; image-text alignment; LLM safety and jailbreak evaluation",
        ),
        (
            "Tools:",
            "Python; PyTorch; Hugging Face Transformers and Diffusers; Jupyter; Git; experiment tracking and reproducible pipelines",
        ),
    ]:
        story.append(
            Paragraph(f"<b>{_escape(label)}</b> {_escape(text)}", styles["SkillLine"])
        )

    doc.build(story)
    print(f"Wrote {PDF_PATH}")


if __name__ == "__main__":
    build_pdf()
