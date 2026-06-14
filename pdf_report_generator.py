from reportlab.pdfgen import canvas
pdf = canvas.Canvas("student_report.pdf")
pdf.setFont("Helvetica-Bold", 16)
pdf.drawString(150, 800, "STUDENT MARKS REPORT")
pdf.setFont("Helvetica", 12)
pdf.drawString(100, 750, "Name      Marks")

pdf.drawString(100, 720, "Ali        85")
pdf.drawString(100, 700, "Aman       92")
pdf.drawString(100, 680, "Sara       78")
pdf.drawString(100, 660, "Riya       88")
pdf.drawString(100, 640, "John       95")

pdf.drawString(100, 580, "Average Marks: 87.6")
pdf.drawString(100, 560, "Highest Marks: 95")
pdf.drawString(100, 540, "Lowest Marks: 78")

pdf.save()
print("PDF Report Generated Successfully!")
