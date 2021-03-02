Attribute VB_Name = "print_pay_statement_to_pdf"
Sub print_pay_statement_to_pdf()

' This VBA module will print a specific Excel tab to a PDF.  The print areas of the tab can be set in the Excel file.
' Multiple tabs and PDFs can be printed by copying the code and setting up new pdf file names.

Worksheets("Statement").Activate
customer_name = ActiveSheet.Cells(9, 7).Value
month = ActiveSheet.Cells(10, 10).Value
day = ActiveSheet.Cells(10, 11).Value
year = ActiveSheet.Cells(10, 12).Value
check_number = ActiveSheet.Cells(12, 7).Value
user_name = ActiveSheet.Cells(17, 17).Value

statement_name = customer_name & " - " & month & "-" & day & "-" & year & " - Check #" & check_number & " Statement.pdf"

' The From and To fields represent the page numbers associated with the printable area on the Excel tab.  Set to higher numbers to capture other numbered pages.
ActiveSheet.ExportAsFixedFormat Type:=xlTypePDF, Filename:="C:\Users\" & user_name & "\Desktop\" & & statement_name, Quality:=xlQualityStandard, _
IncludeDocProperties:=True, IgnorePrintAreas:=False, OpenAfterPublish:=False, From:=1, To:=1

End Sub