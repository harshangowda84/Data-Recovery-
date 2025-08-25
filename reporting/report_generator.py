from reportlab.pdfgen import canvas

class ReportGenerator:
    def generate_pdf(self, case_name, analyst, findings, output_path):
        c = canvas.Canvas(output_path)
        c.drawString(100, 800, f'Case: {case_name}')
        c.drawString(100, 780, f'Analyst: {analyst}')
        y = 760
        for item in findings:
            c.drawString(100, y, str(item))
            y -= 20
        c.save()
