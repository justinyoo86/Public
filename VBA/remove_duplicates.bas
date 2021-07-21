Sub obtain_unique_lot_numbers()

Worksheets("Lot Number Lister").Activate
Columns("J:J").Select
Selection.ClearContents

Worksheets("Completed Workcards").Activate
last_row = Cells(Rows.Count, 2).End(xlUp).Row
Range(Cells(3, 2), Cells(last_row, 2)).Copy

Worksheets("Lot Number Lister").Activate
Range("J2").Select
Selection.PasteSpecial Paste:=xlPasteValues, Operation:=xlNone, SkipBlanks:=False, Transpose:=False
ActiveSheet.Range("$J:$J").RemoveDuplicates Columns:=1, Header:=xlNo

Range("J4").Select
Range(Selection, Selection.End(xlDown)).Select

last_row_in_lot_number = Cells(Rows.Count, 10).End(xlUp).Row

For i = 1 To last_row_in_lot_number
    If IsEmpty(Cells(i, 10)) Then
        Cells(i, 10).Delete Shift:=xlUp
    End If
Next i

Application.CutCopyMode = False

Range("B2").Select
Range(Selection, Selection.End(xlDown)).Select
Selection.ClearContents

Range("J2").Select
Range(Selection, Selection.End(xlDown)).Select
Selection.Copy

Range("B2").Select
Selection.PasteSpecial Paste:=xlPasteValues

Application.CutCopyMode = False

Call copy_unique_lot_numbers_to_clipboard

End Sub