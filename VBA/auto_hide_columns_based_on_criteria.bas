Sub auto_hide_columns_based_on_criteria()

' Author: Justin Yoo
' This VBA module will automatically unhide all rows specified and then hide columns based on a cell's criteria that is within the cell range in the For loop below.

Worksheets("Summary").Select

Rows("1:5000").Select
Selection.EntireRow.Hidden = False

For Each cell In Range("D2:D100")
	If Not IsEmpty(cell) Then
		If cell.Value = 0 Then
			cell.EntireRow.Hidden = True
		End If
	End If
Next

End Sub