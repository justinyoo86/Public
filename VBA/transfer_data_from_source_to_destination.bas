Sub transfer_data_from_source_to_destination()

' This module will copy data ranges from a source_file to a destination_file.  It can be expanded to accomodate multiple ranges across different tabs in both the source_file and destination_file.

Set destination_file = Application.ActiveWorkbook
Set source_file = Application.Workbooks.Open(Application.ActiveWorkbook.Path & "/Source Data.xlsx")
destination_file.Activate

Worksheets("Control_Panel").Activate

import_date = Cells(9, 3).Value

' Activate source_file and copy the data ranges that are to be transferred to the destination_file
source_file.Activate
Worksheets("Root").Activate
last_row_in_root = Cells(Rows.Count, 1).End(xlUp).Row
root_range_1 = Range(Cells(2, 3), Cells(last_row_in_root, 20))
Worksheets("Form Meta Data").Activate
meta_data_range_1 = Range(Cells(2, 2), Cells(last_row_in_root, 3))

' Activate destination_file and paste in the data ranges that were copied from the source_file.
destination_file.Activate
Worksheets("Sites").Activate
last_row_in_sites = Cells(Rows.Count, 2).End(xlUp).Row + 1
Range(Cells(last_row_in_sites, 2), Cells(last_row_in_sites + last_row_in_root - 2, 18)).Value = root_range_1
Range(Cells(last_row_in_sites, 19), Cells(last_row_in_sites + last_row_in_root - 2, 20)).Value = meta_data_range_1
Range(Cells(last_row_in_sites, 22), Cells(last_row_in_sites + last_row_in_root - 2, 22)).Value = import_date

Worksheets("Summary").Activate

source_file.Close

destination_file.Activate

Worksheets("Control_Panel").Activate

End Sub