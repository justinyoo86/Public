Attribute VB_Name = "copy_excel_tables_to_word_document"
Sub copy_excel_tables_to_word_document()

excel_file_path = ActiveWorkbook.Path

' Set variable for the current year
report_name = "\The Monthly Report For "
year = ActiveSheet.Cells(16, 15)

' Set variabls for the current month
month = ActiveSheet.Cells(17, 15)

' Add a zero to the beginning of the month number if it is a single digit month.
If Len(month) = 1 Then
    month = "0" & month
Else
    month = month
End If

'month_word = "July"
month_word = ActiveSheet.Cells(18, 15)

ActiveWorkbook.Save

' The destination Word document needs to be named as follows and located in the same directory file path as the current Excel workbook.
Set object_word = CreateObject("word.Application")
Set object_document = object_word.Documents.Open(file_path & report_name & month & " " & month_word & " " & year & ".docx")

objWord.Visible = True
  
' This will copy and paste a range in Excel as a photo to a bookmark located in a Word Document.  
' This code can be copied multiple times for however many Excel tables need to be copied.
Range(Cells(2, 11), Cells(4, 12)).CopyPicture Appearance:=xlScreen, Format:=xlPicture

' This .Delete line should only be kept in if the report is run on a consistent basis and the existing table from before needs to be deleted.
object_document.Bookmarks("bookmark_1").Range.Delete
object_document.Bookmarks("bookmark_1").Range.Paste

Application.CutCopyMode = False

End Sub