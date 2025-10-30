from fpdf import FPDF

def generar_informe(nombre_pdf, hardening_index, vulnerabilidades):
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Arial", "B", 16)
    pdf.cell(0, 10, "Informe de Auditoría de Seguridad", ln=True, align="C")

    pdf.set_font("Arial", "", 12)
    pdf.ln(10)
    pdf.cell(0, 10, f"Índice de Hardening: {hardening_index}", ln=True)
    pdf.cell(0, 10, f"Total de vulnerabilidades encontradas: {len(vulnerabilidades)}", ln=True)
    pdf.ln(5)

    pdf.set_font("Arial", "B", 12)
    pdf.cell(0, 10, "Detalles de vulnerabilidades:", ln=True)
    pdf.set_font("Arial", "", 11)

    for v in vulnerabilidades:
        pdf.multi_cell(0, 8, f"- [{v['risk']}] {v['alert']} en {v['url']}")

    pdf.output(nombre_pdf)
    print(f"✅ Informe generado: {nombre_pdf}")

# Ejemplo de uso
if __name__ == "__main__":
    hardening = 72
    vulns = [
        {"risk": "Medium", "alert": "SQL Injection", "url": "http://testphp.vulnweb.com/login.php"},
        {"risk": "Low", "alert": "XSS Reflejado", "url": "http://testphp.vulnweb.com/comment.php"},
    ]
    generar_informe("informe_auditoria.pdf", hardening, vulns)
