import os

from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Image
from reportlab.lib.units import inch

from formsbackend import settings


def generate_pdf(form_data, signature_path):
    pdf_path = f'media/anti_harassment/{form_data["printedName"]}_{form_data["date"]}.pdf'
    logo_path = os.path.join(settings.MEDIA_ROOT, 'logo', 'psychiatry_logo.png')

    doc = SimpleDocTemplate(pdf_path, pagesize=letter)
    story = []

    styles = getSampleStyleSheet()
    policy_para = Paragraph(form_data['policyText'], styles['Normal'])
    story.append(policy_para)
    story.append(Spacer(1, 0.2 * inch))

    # Add the text details
    story.append(Paragraph(f"Name: {form_data['printedName']}", styles['Normal']))
    story.append(Paragraph(f"Date: {form_data['date']}", styles['Normal']))
    story.append(Spacer(1, 0.2 * inch))

    # Add the signature image if path is available
    if signature_path:
        signature_img = Image(signature_path)
        signature_img.drawHeight = 1 * inch  # height of the signature image
        signature_img.drawWidth = 3 * inch  # width of the signature image
        story.append(signature_img)
        story.append(Spacer(1, 0.2 * inch))

    # Build the PDF
    doc.build(story)

    return pdf_path
