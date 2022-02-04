Attribute VB_Name = "report_create_report_subroutine"
Sub report_create_audit_report()

Application.Calculation = xlCalculationAutomatic
analysis_file = ActiveWorkbook.Name

Worksheets("Control Panel").Activate

' ID is user_group_id

For user_group_id = 1 To 2
    Worksheets("Control Panel").Activate
    Cells(9, 3) = user_group_id
    user_group = Cells(10, 3).Value
    output_file_path = Cells(6, 3).Value
    output_file_name = Cells(7, 3).Value
            
    Worksheets("Data Summary").Activate
    column_value = Cells(2, 3).Value
    max_run_id = Cells(12, column_value)
    
    Workbooks.Add
    ActiveWorkbook.SaveAs Filename:=output_file_path & output_file_name, FileFormat:=xlOpenXMLWorkbook, CreateBackup:=False
    Sheets("Sheet1").Name = "Summary"
    
    ' Copy and paste the report summary header into the summary report.
    Windows(analysis_file).Activate
    Worksheets("Report").Activate
    Range(Cells(3, 7), Cells(3, 12)).Select
    Selection.Copy
    Windows(output_file_name).Activate
    Worksheets("Summary").Activate
    ActiveSheet.Tab.Color = RGB(0, 176, 80)
    Cells(1, 1).Select
    Selection.PasteSpecial Paste:=xlPasteAllUsingSourceTheme, Operation:=xlNone, SkipBlanks:=False, Transpose:=False
    Selection.PasteSpecial Paste:=xlPasteValues, Operation:=xlNone, SkipBlanks:=False, Transpose:=False

    ' Iterate through and begin copying and pasting the tabs.
    Windows(analysis_file).Activate
    Worksheets("Data Summary").Activate
    
    For run_id = 1 To max_run_id
        Worksheets("Data Summary").Activate
        Cells(4, column_value) = run_id
        tab_name = Cells(5, column_value).Value
        user_group_name = Cells(20, column_value).Value
        output_file_yes_or_no = Cells(21, column_value).Value
        output_report_tab_name = Cells(22, column_value).Value
        output_report_frequency = Cells(23, column_value).Value
        
        If user_group_name = user_group And output_file_yes_or_no = "Yes" Then
            column_value = Cells(2, 3).Value
            tab_name = Cells(5, column_value).Value
            Worksheets(tab_name).Activate
            
            For last_column = 1 To 100
                If IsEmpty(Cells(2, last_column)) Then
                    last_column_found = last_column
                    Exit For
                End If
            Next last_column
            
            For column_number = 1 To 100
                If Not (Cells(3, column_number).HasFormula) Then
                    last_row = Cells(Rows.Count, column_number).End(xlUp).Row
                    Range(Cells(2, column_number), Cells(last_row, last_column_found)).Select
                    Selection.Copy
                    Exit For
                Else
                End If
            Next column_number
            
            ' Create a new tab in the summary report and paste in the data from the audit file.
            Windows(output_file_name).Activate
            Sheets.Add After:=ActiveSheet
            ActiveSheet.Name = output_report_tab_name
            ' Change tab color
            If output_report_frequency = "Daily" Then
                ActiveSheet.Tab.Color = RGB(146, 208, 80)
            ElseIf output_report_frequency = "Weekly" Then
                ActiveSheet.Tab.Color = RGB(255, 196, 0)
            ElseIf output_report_frequency = "Monthly" Then
                ActiveSheet.Tab.Color = RGB(255, 255, 0)
            End If
            
            Cells(1, 1).Select
            Selection.PasteSpecial Paste:=xlPasteAllUsingSourceTheme, Operation:=xlNone, SkipBlanks:=False, Transpose:=False
            Selection.PasteSpecial Paste:=xlPasteValues, Operation:=xlNone, SkipBlanks:=False, Transpose:=False
            Selection.Columns.AutoFit
            Cells(1, 1).Select
            Sheets("Summary").Activate
            
            ' Copy and paste the summary table row
            Windows(analysis_file).Activate
            Sheets("Report").Activate
            
            summary_run_id_range = Range(Cells(4, 2), Cells(100, 3))
                        
            For i = 1 To 90
                If summary_run_id_range(i, 1) = run_id Then
                    Range(Cells(summary_run_id_range(i, 2), 7), Cells(summary_run_id_range(i, 2), 12)).Select
                    Selection.Copy
                    Windows(output_file_name).Activate
                    Sheets("Summary").Activate
                    last_row = Cells(Rows.Count, 1).End(xlUp).Row + 1
                    Cells(last_row, 1).Select
                    Selection.PasteSpecial Paste:=xlPasteAllUsingSourceTheme, Operation:=xlNone, SkipBlanks:=False, Transpose:=False
                    Selection.PasteSpecial Paste:=xlPasteValues, Operation:=xlNone, SkipBlanks:=False, Transpose:=False
                    Cells(1, 1).Select
                    Range(ActiveCell, ActiveCell.End(xlDown).End(xlToRight)).Select
                    Selection.Columns.AutoFit
                    Cells(1, 1).Select
                    Windows(analysis_file).Activate
                Else
                End If
            Next i
            
            Windows(analysis_file).Activate
            
        End If

    Next run_id

Windows(output_file_name).Activate
ActiveWorkbook.Save
ActiveWorkbook.Close

Next user_group_id


Windows(analysis_file).Activate
Cells(1, 1).Select
Worksheets("Control Panel").Activate

End Sub
