Public Function HVAC_Unit_Age(Make As String, Serial As String)

' This function will calculate the age of an HVAC unit when inputting in the Make and Serial Number (as Serial).
' Example Formula text =IF(ISBLANK($AO4),IFERROR(HVAC_Unit_Age(X4,AA4),""),$AO4)

If Make = "" Then
    HVAC_Unit_Age = ""
    GoTo End_Line
End If

Error_Message = "Unknown - Please Debug Serial Number or Code"

If Len(Serial) <= 6 Then
    HVAC_Unit_Age = "Unknown - Need a full Serial Number"
    GoTo End_Line
End If

First_Character = Left(Serial, 1)
Second_Character = Mid(Serial, 2, 1)
Third_Character = Mid(Serial, 3, 1)
Fourth_Character = Mid(Serial, 4, 1)
Fifth_Character = Mid(Serial, 5, 1)
Sixth_Character = Mid(Serial, 6, 1)

First_Character_Boolean = IsNumeric(First_Character)
Second_Character_Boolean = IsNumeric(Second_Character)
Third_Character_Boolean = IsNumeric(Third_Character)
Fourth_Character_Boolean = IsNumeric(Fourth_Character)
Fifth_Character_Boolean = IsNumeric(Fifth_Character)
Sixth_Character_Boolean = IsNumeric(Sixth_Character)

If First_Character_Boolean = "True" Then
    First_Character_Boolean = 1
Else
    First_Character_Boolean = 0
End If

If Second_Character_Boolean = "True" Then
    Second_Character_Boolean = 1
Else
    Second_Character_Boolean = 0
End If

If Third_Character_Boolean = "True" Then
    Third_Character_Boolean = 1
Else
    Third_Character_Boolean = 0
End If

If Fourth_Character_Boolean = "True" Then
    Fourth_Character_Boolean = 1
Else
    Fourth_Character_Boolean = 0
End If

If Fifth_Character_Boolean = "True" Then
    Fifth_Character_Boolean = 1
Else
    Fifth_Character_Boolean = 0
End If

If Sixth_Character_Boolean = "True" Then
    Sixth_Character_Boolean = 1
Else
    Sixth_Character_Boolean = 0
End If


All_Boolean_Code = First_Character_Boolean & Second_Character_Boolean & Third_Character_Boolean & Fourth_Character_Boolean



If Make = "York" Or Make = "Unitary Products" Then
    If All_Boolean_Code = "0101" Then
        HVAC_Unit_Age = Second_Character + Fourth_Character + 2000
    ElseIf All_Boolean_Code = "0000" Then
        If Third_Character = "A" Then
            HVAC_Unit_Age = 1992
        ElseIf Third_Character = "B" Then
            HVAC_Unit_Age = 1993
        ElseIf Third_Character = "C" Then
            HVAC_Unit_Age = 1994
        ElseIf Third_Character = "D" Then
            HVAC_Unit_Age = 1995
        ElseIf Third_Character = "E" Then
            HVAC_Unit_Age = 1996
        ElseIf Third_Character = "F" Then
            HVAC_Unit_Age = 1997
        ElseIf Third_Character = "G" Then
            HVAC_Unit_Age = 1998
        ElseIf Third_Character = "H" Then
            HVAC_Unit_Age = 1999
        ElseIf Third_Character = "J" Then
            HVAC_Unit_Age = 2000
        ElseIf Third_Character = "K" Then
            HVAC_Unit_Age = 2001
        ElseIf Third_Character = "L" Then
            HVAC_Unit_Age = 2002
        ElseIf Third_Character = "M" Then
            HVAC_Unit_Age = 2003
        ElseIf Third_Character = "N" Then
            HVAC_Unit_Age = 2004
        ElseIf Third_Character = "P" Then
            HVAC_Unit_Age = 1984
        ElseIf Third_Character = "R" Then
            HVAC_Unit_Age = 1985
        ElseIf Third_Character = "S" Then
            HVAC_Unit_Age = 1986
        ElseIf Third_Character = "T" Then
            HVAC_Unit_Age = 1987
        ElseIf Third_Character = "V" Then
            HVAC_Unit_Age = 1988
        ElseIf Third_Character = "W" Then
            HVAC_Unit_Age = 1989
        ElseIf Third_Character = "X" Then
            HVAC_Unit_Age = 1990
        ElseIf Third_Character = "Y" Then
            HVAC_Unit_Age = 1991
        End If
    Else
        HVAC_Unit_Age = Error_Message
    End If
    
ElseIf Make = "Trane" Then
    If Len(Serial) = 9 And IsNumeric(Left(Serial, 1)) Then
        HVAC_Unit_Age = 2000 + Left(Serial, 1)
    ElseIf All_Boolean_Code = "0110" Or All_Boolean_Code = "0111" Then
        If First_Character = "W" Then
            HVAC_Unit_Age = 1983
        ElseIf First_Character = "X" Then
            HVAC_Unit_Age = 1984
        ElseIf First_Character = "Y" Then
            HVAC_Unit_Age = 1985
        ElseIf First_Character = "Z" Then
            HVAC_Unit_Age = 1986
        ElseIf First_Character = "B" Then
            HVAC_Unit_Age = 1987
        ElseIf First_Character = "C" Then
            HVAC_Unit_Age = 1988
        ElseIf First_Character = "D" Then
            HVAC_Unit_Age = 1989
        ElseIf First_Character = "E" Then
            HVAC_Unit_Age = 1990
        ElseIf First_Character = "F" Then
            HVAC_Unit_Age = 1991
        ElseIf First_Character = "G" Then
            HVAC_Unit_Age = 1992
        ElseIf First_Character = "H" Then
            HVAC_Unit_Age = 1993
        ElseIf First_Character = "J" Then
            HVAC_Unit_Age = 1994
        ElseIf First_Character = "K" Then
            HVAC_Unit_Age = 1995
        ElseIf First_Character = "L" Then
            HVAC_Unit_Age = 1996
        ElseIf First_Character = "M" Then
            HVAC_Unit_Age = 1997
        ElseIf First_Character = "N" Then
            HVAC_Unit_Age = 1998
        ElseIf First_Character = "P" Then
            HVAC_Unit_Age = 1999
        ElseIf First_Character = "R" Then
            HVAC_Unit_Age = 2000
        ElseIf First_Character = "S" Then
            HVAC_Unit_Age = 2001
        End If
    Else
        HVAC_Unit_Age = 2000 + Left(Serial, 2)
    End If

ElseIf Make = "American Standard" Then
    If All_Boolean_Code = "0111" Then
        If First_Character = "W" Then
            HVAC_Unit_Age = 1983
        ElseIf First_Character = "X" Then
            HVAC_Unit_Age = 1984
        ElseIf First_Character = "Y" Then
            HVAC_Unit_Age = 1985
        ElseIf First_Character = "Z" Then
            HVAC_Unit_Age = 1986
        ElseIf First_Character = "B" Then
            HVAC_Unit_Age = 1987
        ElseIf First_Character = "C" Then
            HVAC_Unit_Age = 1988
        ElseIf First_Character = "D" Then
            HVAC_Unit_Age = 1989
        ElseIf First_Character = "E" Then
            HVAC_Unit_Age = 1990
        ElseIf First_Character = "F" Then
            HVAC_Unit_Age = 1991
        ElseIf First_Character = "G" Then
            HVAC_Unit_Age = 1992
        ElseIf First_Character = "H" Then
            HVAC_Unit_Age = 1993
        ElseIf First_Character = "J" Then
            HVAC_Unit_Age = 1994
        ElseIf First_Character = "K" Then
            HVAC_Unit_Age = 1995
        ElseIf First_Character = "L" Then
            HVAC_Unit_Age = 1996
        ElseIf First_Character = "M" Then
            HVAC_Unit_Age = 1997
        ElseIf First_Character = "N" Then
            HVAC_Unit_Age = 1998
        ElseIf First_Character = "P" Then
            HVAC_Unit_Age = 1999
        ElseIf First_Character = "R" Then
            HVAC_Unit_Age = 2000
        ElseIf First_Character = "S" Then
            HVAC_Unit_Age = 2001
        End If
    ElseIf All_Boolean_Code = "1111" Then
        HVAC_Unit_Age = 2000 + Left(Serial, 1)
    End If


ElseIf Make = "Lennox" Or Make = "Carrier" Or Make = "Gree" Or Make = "Payne" Or Make = "Bryant" Then
    If Mid(Serial, 3, 2) >= 30 Then
        HVAC_Unit_Age = 1900 + Mid(Serial, 3, 2)
    Else
        HVAC_Unit_Age = 2000 + Mid(Serial, 3, 2)
    End If
    
ElseIf Make = "Goodman" Or Make = "Amana" Or Make = "RV products" Then
    If Mid(Serial, 1, 2) >= 30 Then
        HVAC_Unit_Age = 1900 + Mid(Serial, 1, 2)
    Else
        HVAC_Unit_Age = 2000 + Mid(Serial, 1, 2)
    End If

ElseIf Make = "ICP (International Comfort Products)" Then
    If Mid(Serial, 2, 2) >= 30 Then
        HVAC_Unit_Age = 1900 + Mid(Serial, 2, 2)
    Else
        HVAC_Unit_Age = 2000 + Mid(Serial, 2, 2)
    End If
    
ElseIf Make = "Bard" Then
    If All_Boolean_Code = "1110" Or All_Boolean_Code = "0010" Then
        If Mid(Serial, 5, 2) >= 30 Then
            HVAC_Unit_Age = 1900 + Mid(Serial, 5, 2)
        Else
            HVAC_Unit_Age = 2000 + Mid(Serial, 5, 2)
        End If
    End If
    
    
ElseIf Make = "Day and Night" Then
    If Not IsNumeric(Left(Serial, 1)) Then
        If Mid(Serial, 2, 2) >= 30 Then
            HVAC_Unit_Age = 1900 + Mid(Serial, 2, 2)
        Else
            HVAC_Unit_Age = 2000 + Mid(Serial, 2, 2)
        End If
    Else
        If Mid(Serial, 3, 2) >= 30 Then
            HVAC_Unit_Age = 1900 + Mid(Serial, 3, 2)
        Else
            HVAC_Unit_Age = 2000 + Mid(Serial, 3, 2)
        End If
    End If
    
ElseIf Make = "Coleman" Then
    If All_Boolean_Code = "0101" Then
        HVAC_Unit_Age = Second_Character + Fourth_Character + 2000
    ElseIf All_Boolean_Code = "1111" Then
        If Mid(Serial, 1, 2) >= 30 Then
            HVAC_Unit_Age = 1900 + Mid(Serial, 1, 2)
        Else
            HVAC_Unit_Age = 2000 + Mid(Serial, 1, 2)
        End If
    End If
    
ElseIf Make = "Revolv" Then
    If All_Boolean_Code = "0001" Then
        HVAC_Unit_Age = Fourth_Character + Fifth_Character + 2000
    ElseIf All_Boolean_Code = "0101" Then
        If First_Character = "W" Then
            HVAC_Unit_Age = Second_Character + Fourth_Character + 2000
        Else
            If Mid(Serial, 4, 2) >= 30 Then
                HVAC_Unit_Age = 1900 + Mid(Serial, 4, 2)
            Else
                HVAC_Unit_Age = 2000 + Mid(Serial, 4, 2)
            End If
        End If
    End If
    
ElseIf Make = "Nordyne" Or Make = "Nortek" Then
    If All_Boolean_Code = "0001" Then
        HVAC_Unit_Age = Fourth_Character + Fifth_Character + 2000
    ElseIf All_Boolean_Code = "0101" Then
        HVAC_Unit_Age = Fourth_Character + Fifth_Character + 2000
    End If

ElseIf Make = "RUUD" Or Make = "Rheem" Then
    If All_Boolean_Code = "1111" Then
        HVAC_Unit_Age = 2000 + Mid(Serial, 8, 2)
    ElseIf All_Boolean_Code = "0111" Then
        HVAC_Unit_Age = 2000 + Mid(Serial, 4, 2)
    End If
    
ElseIf Make = "HEIL" Then
    If All_Boolean_Code = "0111" Then
        If Mid(Serial, 2, 2) >= 30 Then
            HVAC_Unit_Age = 1900 + Mid(Serial, 2, 2)
        Else
            HVAC_Unit_Age = 2000 + Mid(Serial, 2, 2)
        End If
    End If

ElseIf Make = "Ducane" Then
    If Not IsNumeric(Left(Serial, 5)) Then
        If Mid(Serial, 3, 2) >= 30 Then
                HVAC_Unit_Age = 1900 + Mid(Serial, 3, 2)
            Else
                HVAC_Unit_Age = 2000 + Mid(Serial, 3, 2)
        End If
    ElseIf All_Boolean_Code = "1111" Then
        HVAC_Unit_Age = 2000 + Mid(Serial, 1, 1)
    End If
    
ElseIf Make = "Daikin" Then
    If Not IsNumeric(Left(Serial, 1)) Then
        If Mid(Serial, 4, 2) >= 30 Then
                HVAC_Unit_Age = 1900 + Mid(Serial, 4, 2)
            Else
                HVAC_Unit_Age = 2000 + Mid(Serial, 4, 2)
        End If
    ElseIf All_Boolean_Code = "1111" Then
        HVAC_Unit_Age = 2000 + Mid(Serial, 1, 2)
    End If
    
End If

If HVAC_Unit_Age >= 2022 Then
    HVAC_Unit_Age = "Unknown - Please Debug Serial Number or Code"
End If

End Function