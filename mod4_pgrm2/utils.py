import csv
from reportlab.pdfgen import canvas
from django.http import HttpResponse

def generate_csv_response(queryset, filename):
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = f'attachment; filename="{filename}.csv"'
    writer = csv.writer(response)
    
    # Write header row based on model fields
    writer.writerow([field.name for field in queryset.model._meta.fields])
    
    # Write data rows
    for obj in queryset:
        writer.writerow([getattr(obj, field.name) for field in queryset.model._meta.fields])
    
    return response

def generate_pdf_response(queryset, filename):
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = f'attachment; filename="{filename}.pdf"'
    
    # Create PDF document
    pdf = canvas.Canvas(response)
    y = 800 # Initial y position for writing text

    # Write header
    pdf.setFont("Helvetica-Bold", 12)
    pdf.drawString(100, y, "Student Data")

    # Write data
    pdf.setFont("Helvetica", 10)
    y -= 20 # Move down for data rows

    for obj in queryset:
        data = f"Name: {obj.name}, Email: {obj.email}" # Customize based on your model fields
        pdf.drawString(100, y, data)
        y -= 15 # Move down for next row

        courses = obj.courses.all()
        if courses:
            pdf.setFont("Helvetica-Bold", 10)
            pdf.drawString(120, y, "Courses:")
            y -= 15
            pdf.setFont("Helvetica", 10)
            for course in courses:
                course_info = f"- {course.name}: {course.description}"
                pdf.drawString(140, y, course_info)
                y -= 15
        else:
            pdf.setFont("Helvetica-Bold", 10)
            pdf.drawString(120, y, "Courses: None")
            y -= 15

        y -= 15 # Add extra space between students

        # Check for page overflow
        if y < 40:
            pdf.showPage()
            pdf.setFont("Helvetica", 10)
            y = 750
    
    pdf.showPage()
    pdf.save()
    return response
