Sub obtain_summary_board()

Worksheets("Summary List").Activate
Selection.AutoFilter


Columns("A:H").Select
Selection.Clear

Worksheets("Completed Workcards").Activate
last_row = Cells(Rows.Count, 11).End(xlUp).Row
Range(Cells(2, 1), Cells(last_row, 9)).Copy

Worksheets("Summary List").Activate
Range("A1").Select
Selection.PasteSpecial Paste:=xlPasteFormats
Selection.PasteSpecial Paste:=xlPasteValues
Selection.RemoveDuplicates Columns:=Array(1, 2, 3, 4, 5, 6, 7, 8, 9), Header:=xlYes

last_row_columns = Cells(Rows.Count, 1).End(xlUp).Row
Range(Cells(2, 9), Cells(last_row_columns, 11)).Select

'Create borders for selected cells.

Selection.Borders(xlDiagonalDown).LineStyle = xlNone
    Selection.Borders(xlDiagonalUp).LineStyle = xlNone
    With Selection.Borders(xlEdgeLeft)
        .LineStyle = xlContinuous
        .ColorIndex = 0
        .TintAndShade = 0
        .Weight = xlThin
    End With
    With Selection.Borders(xlEdgeTop)
        .LineStyle = xlContinuous
        .ColorIndex = 0
        .TintAndShade = 0
        .Weight = xlThin
    End With
    With Selection.Borders(xlEdgeBottom)
        .LineStyle = xlContinuous
        .ColorIndex = 0
        .TintAndShade = 0
        .Weight = xlThin
    End With
    With Selection.Borders(xlEdgeRight)
        .LineStyle = xlContinuous
        .ColorIndex = 0
        .TintAndShade = 0
        .Weight = xlThin
    End With
    With Selection.Borders(xlInsideVertical)
        .LineStyle = xlContinuous
        .ColorIndex = 0
        .TintAndShade = 0
        .Weight = xlThin
    End With
    With Selection.Borders(xlInsideHorizontal)
        .LineStyle = xlContinuous
        .ColorIndex = 0
        .TintAndShade = 0
        .Weight = xlThin
    End With

Cells(1, 1).Select

If ActiveSheet.FilterMode = True Then
ElseIf ActiveSheet.FilterMode = False Then
    Selection.AutoFilter
End If

ActiveWorkbook.Worksheets("Summary List").AutoFilter.Sort.SortFields.Add Key:= _
        Range("E:E"), SortOn:=xlSortOnValues, Order:=xlDescending, DataOption _
        :=xlSortNormal

With ActiveWorkbook.Worksheets("Summary List").AutoFilter.Sort
        .Header = xlYes
        .MatchCase = False
        .Orientation = xlTopToBottom
        .SortMethod = xlPinYin
        .Apply
End With

ActiveSheet.Range("A1:K1").AutoFilter Field:=5, Criteria1:=Array(">=0"), Operator:=xlAnd

With ActiveWorkbook.Worksheets("Summary List").AutoFilter.Sort
        .Header = xlYes
        .MatchCase = False
        .Orientation = xlTopToBottom
        .SortMethod = xlPinYin
        .Apply
End With

ActiveWorkbook.Worksheets("Summary List").AutoFilter.Sort.SortFields.Clear

ActiveWorkbook.Worksheets("Summary List").AutoFilter.Sort.SortFields.Add2 Key:= _
        Range("F:F"), SortOn:=xlSortOnValues, Order:=xlAscending, DataOption _
        :=xlSortNormal

With ActiveWorkbook.Worksheets("Summary List").AutoFilter.Sort
        .Header = xlYes
        .MatchCase = False
        .Orientation = xlTopToBottom
        .SortMethod = xlPinYin
        .Apply
End With


End Sub