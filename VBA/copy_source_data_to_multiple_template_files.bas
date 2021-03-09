Sub copy_source_data_to_multiple_template_files()

' Author: Justin Yoo
' This VBA module will copy and paste ranged data from a source file to a template file through iteration.  The template files will be customized by site and saved by site number.
' The copy and paste ranges will need to be set for both the source file and the template files.  

source_file = "Tracking Sheet.xlsm"
source_file_tab = "Source Tab"
output_file_path = "C:\Users\user\Documents\"
output_file_name_prefix = " Tool v1.0 - "
template_file = "C:\Users\user\Documents\Template File.xlsm"

work_order = "A"

Workbooks(source_file).Activate
Worksheets(source_file_tab).Activate

number_of_sites = ActiveSheet.Cells(3, 2)

For i = 1 To number_of_sites
    Workbooks(source_file).Activate
    Worksheets(source_file_tab).Activate
    
    ActiveSheet.Cells(2, 1) = i
    
    client_name = ActiveSheet.Cells(3, 4)
    customer_id = ActiveSheet.Cells(2, 28)
    site_number = ActiveSheet.Cells(2, 2)
	
	If Len(site_number) = 3 Then
        site_number = "00" & site_number
    ElseIf Len(SiteNumber) = 4 Then
        site_number = "0" & site_number
    End If
	
    address = ActiveSheet.Cells(2, 3)
    city = ActiveSheet.Cells(2, 4)
    zip = ActiveSheet.Cells(2, 6)
    account_number = ActiveSheet.Cells(2, 27)
    business_name = ActiveSheet.Cells(2, 8)
    business_address = ActiveSheet.Cells(2, 9)
    business_city = ActiveSheet.Cells(2, 10)
    business_state = ActiveSheet.Cells(2, 11)
    business_zip = ActiveSheet.Cells(2, 12)
    business_phone_number = ActiveSheet.Cells(2, 13)
    business_annual_kwh = ActiveSheet.Cells(2, 14)
    business_annual_therms = ActiveSheet.Cells(2, 15)
    square_footage = ActiveSheet.Cells(2, 16)
    energy_assessment_date = ActiveSheet.Cells(2, 17)
    hours_on_per_day = ActiveSheet.Cells(2, 18)
    store_number = ActiveSheet.Cells(2, 19)
    time_open = ActiveSheet.Cells(2, 21)
    time_closed = ActiveSheet.Cells(2, 22)
    
    Worksheets("Clipboard").Activate
    
    Set hvac_replacement_range_1 = ActiveSheet.Range(Cells(7, 5), Cells(13, 13))
    
    Set economizer_dcv_range_1 = ActiveSheet.Range(Cells(27, 5), Cells(40, 7))
    
    Set vfd_range_1 = ActiveSheet.Range(Cells(49, 5), Cells(55, 7))
    
	Set template_workbook = Application.Workbooks.Open(template_file)
    template_workbook.Activate
    
	Worksheets("Customer Information").Activate
    
    'Paste Unique Values into the Cells
    ActiveSheet.Cells(2, 7) = customer_id
    ActiveSheet.Cells(5, 1) = account_number
    ActiveSheet.Cells(5, 2) = work_order
    ActiveSheet.Cells(5, 3) = business_name
    ActiveSheet.Cells(5, 4) = business_address
    ActiveSheet.Cells(5, 5) = business_city
    ActiveSheet.Cells(5, 6) = business_state
    ActiveSheet.Cells(5, 7) = business_zip
    ActiveSheet.Cells(5, 8) = business_phone_number
    ActiveSheet.Cells(11, 4) = hours_on_per_day
    ActiveSheet.Cells(14, 3) = energy_assessment_date
    ActiveSheet.Cells(17, 1) = business_annual_kwh
    ActiveSheet.Cells(17, 4) = store_number
    ActiveSheet.Cells(17, 5) = business_address
    ActiveSheet.Cells(17, 6) = business_city
    ActiveSheet.Cells(17, 7) = business_state
    ActiveSheet.Cells(17, 8) = business_zip
    ActiveSheet.Cells(17, 9) = business_phone_number
    ActiveSheet.Cells(20, 3) = time_open
    ActiveSheet.Cells(20, 4) = time_closed
    ActiveSheet.Cells(20, 7) = business_annual_therms
    ActiveSheet.Cells(23, 1) = square_footage
    
    Worksheets("HVAC").Activate
    ActiveSheet.Range(Cells(6, 1), Cells(12, 9)).Value = hvac_replacement_range_1.Value
    ActiveSheet.Range(Cells(25, 1), Cells(38, 3)).Value = economizer_dcv_range_1.Value
    ActiveSheet.Range(Cells(64, 1), Cells(70, 3)).Value = vfd_range_1.Value
    
	Worksheets("Summary Report").Activate
    template_workbook.SaveAs (output_file_path & output_file_name_prefix & client_name & " " & site_number & ".xlsm")
    template_workbook.Close
    
Next i

End Sub