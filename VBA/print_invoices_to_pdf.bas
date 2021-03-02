Attribute VB_Name = "print_invoices_to_pdf"
Sub print_invoice_to_pdf()

' This VBA module will print a specific Excel tab to a PDF.  The print areas of the tab can be set in the Excel file.
' Multiple tabs and PDFs can be printed by copying the code and setting up new pdf file names.

Worksheets("Invoicer").Activate
project_number = ActiveSheet.Cells(25, 3).Value
project_id = ActiveSheet.Cells(25, 2).Value
user_name = ActiveSheet.Cells(17, 17).Value

invoice_file_name = project_number & " - Invoice.pdf"

' The From and To fields represent the page numbers associated with the printable area on the Excel tab.  Set to higher numbers to capture other numbered pages.
ActiveSheet.ExportAsFixedFormat Type:=xlTypePDF, Filename:="C:\Users\" & user_name & "\Desktop\" & project_id & " - " & invoice_file_name, Quality:=xlQualityStandard, _
IncludeDocProperties:=True, IgnorePrintAreas:=False, OpenAfterPublish:=False, From:=1, To:=1

End Sub