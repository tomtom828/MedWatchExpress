import os
import pdfrw

import base64

# INVOICE_TEMPLATE_PATH = '/Users/tommy/Desktop/PDF-Hack/invoice_template.pdf'
INVOICE_TEMPLATE_PATH = '/Users/tommy/Desktop/PDF-Hack/FDA-3500_508-Template.pdf'
INVOICE_OUTPUT_PATH = '/Users/tommy/Desktop/PDF-Hack/invoice_filled.pdf'


ANNOT_KEY = '/Annots'
ANNOT_FIELD_KEY = '/T'
ANNOT_VAL_KEY = '/V'
ANNOT_RECT_KEY = '/Rect'
SUBTYPE_KEY = '/Subtype'
WIDGET_SUBTYPE_KEY = '/Widget'


def write_fillable_pdf(input_pdf_path, output_pdf_path, data_dict):
    template_pdf = pdfrw.PdfReader(input_pdf_path)
    annotations = template_pdf.pages[0][ANNOT_KEY]
    for annotation in annotations:
        if annotation[SUBTYPE_KEY] == WIDGET_SUBTYPE_KEY:
            if annotation[ANNOT_FIELD_KEY]:
                key = annotation[ANNOT_FIELD_KEY][1:-1]
                if key in data_dict.keys():
                    annotation.update(
                        pdfrw.PdfDict(V='{}'.format(data_dict[key]))
                    )
    pdfrw.PdfWriter().write(output_pdf_path, template_pdf)



def read_fillable_pdf(input_pdf_path):
  template_pdf = pdfrw.PdfReader(input_pdf_path)
  annotations = template_pdf.pages[0][ANNOT_KEY]
  i = 0
  for annotation in annotations:
      if annotation[SUBTYPE_KEY] == WIDGET_SUBTYPE_KEY:
          if annotation[ANNOT_FIELD_KEY]:
            key = annotation['/T'][1:-1]
            print('id=',i,'key=',key)
            i+=1



def read_fillable_pdf2(input_pdf_path,output_pdf_path, data_dict):
  template_pdf = pdfrw.PdfReader(input_pdf_path)
  annotations = template_pdf.pages[0][ANNOT_KEY]
  i = 0
  for annotation in annotations:
    if annotation[SUBTYPE_KEY] == WIDGET_SUBTYPE_KEY:
      if annotation[ANNOT_FIELD_KEY]:
        key = annotation['/T'][1:-1]
        # if parsedKey=='death_year':
        # print('id=',i,'key=',key)
        if (i==22):
          print("before: ",annotation)
          annotation.update(pdfrw.PdfDict(AS='/1'))
          print('id=',i,'key=',key)
          print('after: ', annotation)
          # annotation.update(pdfrw.PdfDict(V=pdfrw.PdfName('Y')))
    i+=1
  pdfrw.PdfWriter().write(output_pdf_path, template_pdf)



data_dict_old = {
   'business_name_1': 'Bostata',
   'customer_name': 'company.io',
   'customer_email': 'joe@company.io',
   'invoice_number': '102394',
   'send_date': '2018-02-13',
   'due_date': '2018-03-13',
   'note_contents': 'Thank you for your business, Joe',
   'item_1': 'Data consulting services',
   'item_1_quantity': '10 hours',
   'item_1_price': '$200/hr',
   'item_1_amount': '$2000',
   'subtotal': '$2000',
   'tax': '0',
   'discounts': '0',
   'total': '$2000',
   'business_name_2': 'Bostata LLC',
   'business_email_address': 'hi@bostata.com',
   'business_phone_number': '(617) 930-4294'
}


data_dict = {
  0: 'event_day[0]',
  1: 'event_month[0]',
  2: 'event_year[0]',
  3: 'report_day[0]',
  4: 'report_month[0]',
  5: 'report_year[0]',
  6: 'Patient_Identifier[0]',
  7: 'fda_rec_date[0]',
  8: 'triage_unit[0]',
  9: 'weight[0]',
  10: 'male_box[0]',
  11: 'female_box[0]',
  12: 'problem_manufacturer[0]',
  13: 'product_problem[0]',
  14: 'use_error[0]',
  15: 'adverse_event[0]',
  16: 'outcome_other[0]',
  17: 'birth_defect[0]',
  18: 'disability[0]',
  19: 'intervention[0]',
  20: 'hospital_box[0]',
  21: 'life_threatening_box[0]',
  22: 'death_box[0]',
  23: 'Other_Relevant_Tests[0]',
  24: 'Relevant_Tests[0]',
  25: 'Describe_Problem[0]',
  26: 'Returned[0]',
  27: 'available_no[0]',
  28: 'available_yes[0]',
  29: 'Manufacturer2[0]',
  30: 'NameStrength2[0]',
  31: 'Manufacturer1[0]',
  32: 'NameStrength1[0]',
  33: 'patient_age[0]',
  34: 'age_years[0]',
  35: 'age_months[0]',
  36: 'age_weeks[0]',
  37: 'age_days[0]',
  38: 'weight_lb[0]',
  39: 'weight_kg[0]',
  40: 'ethnicity_yes[0]',
  41: 'ethnicity_no[0]',
  42: 'race_asian[0]',
  43: 'race_american[0]',
  44: 'race_african[0]',
  45: 'race_european[0]',
  46: 'race_pacific[0]',
  47: 'NDC1[0]',
  48: 'lot1[0]',
  49: 'lot1[1]',
  50: 'NDC1[1]',
  51: 'Dose1[0]',
  52: 'Frequency1[0]',
  53: 'Route1[0]',
  54: 'Dose2[0]',
  55: 'Frequency2[0]',
  56: 'Route2[0]',
  57: 'Diagnosis2[0]',
  58: 'Diagnosis1[0]',
  59: 'UseDate1[0]',
  60: 'UseDate2[0]',
  61: 'compounded_yes_01[0]',
  62: 'compounded_no_01[0]',
  63: 'compounded_no_02[0]',
  64: 'compounded_yes_02[0]',
  65: 'overthecounter_yes_01[0]',
  66: 'overthecounter_no_01[0]',
  67: 'overthecounter_no_02[0]',
  68: 'overthecounter_yes_02[0]',
  69: 'abated_na_02[0]',
  70: 'abated_no_01[0]',
  71: 'abated_na_01[0]',
  72: 'abated_yes_01[0]',
  73: 'abated_yes_02[0]',
  74: 'abated_no_02[0]',
  75: 'reappeared_yes_01[0]',
  76: 'reappeared_yes_02[0]',
  77: 'reappeared_no_01[0]',
  78: 'reappeared_no_02[0]',
  79: 'reappeared_na_01[0]',
  80: 'reappeared_na_02[0]',
  81: 'Other_No[0]',
  82: 'Serial_No[0]',
  83: 'Catalog_No[0]',
  84: 'Lot_No[0]',
  85: 'Model_No[0]',
  86: 'Manufacturer_Name[0]',
  87: 'Procode[0]',
  88: 'Device_Name[0]',
  89: 'Brand_Name[0]',
  90: 'Operator_Other[0]',
  91: 'operator_other[0]',
  92: 'lay_user[0]',
  93: 'health_prof[0]',
  94: 'single_use_no[0]',
  95: 'single_use_yes[0]',
  96: 'Reprocessor_Info[0]',
  97: 'Concomitant[0]',
  98: 'G1_Last_Name[0]',
  99: 'G1_First_Name[0]',
  100: 'G1_ZIP[0]',
  101: 'G1_State[0]',
  102: 'G1_City[0]',
  103: 'G1_Address[0]',
  104: 'G1_Country[0]',
  105: 'G1_Email[0]',
  106: 'G1_Phone[0]',
  107: 'Distributor_Importer[0]',
  108: 'User_Facility[0]',
  109: 'Manufacturer[0]',
  110: 'Identity[0]',
  111: 'OCCUPATION[0]',
  112: 'chkHealthNo[0]',
  113: 'chkHealthYes[0]',
  114: 'Reset_Form[0]',
  115: '__Continue_on_page_2_[0]',
  116: '__Continue_on_page_2_[1]',
  117: '__Continue_on_page_2_[2]',
  118: '__Continue_on_page_2_[3]',
  119: 'patient_dob_day[0]',
  120: 'patient_dob_month[0]',
  121: 'patient_dob_year[0]',
  122: 'death_day[0]',
  123: 'death_month[0]',
  124: 'death_year[0]',
  125: 'return_day[0]',
  126: 'return_month[0]',
  127: 'return_year[0]',
  128: 'product_expiration_day_01[0]',
  129: 'product_expiration_month_01[0]',
  130: 'product_expiration_year_01[0]',
  131: 'product_expiration_day_02[0]',
  132: 'product_expiration_month_02[0]',
  133: 'product_expiration_year_02[0]',
  134: 'device_expiration_day_01[0]',
  135: 'device_expiration_month_01[0]',
  136: 'device_expiration_year_01[0]',
  137: 'implant_day_01[0]',
  138: 'implant_month_01[0]',
  139: 'implant_year_01[0]',
  140: 'explant_day_01[0]',
  141: 'explant_month_01[0]',
  142: 'explant_year_01[0]'
}

if __name__ == '__main__':
    # write_fillable_pdf(INVOICE_TEMPLATE_PATH, INVOICE_OUTPUT_PATH, data_dict)
    read_fillable_pdf2(INVOICE_TEMPLATE_PATH, INVOICE_OUTPUT_PATH, data_dict)

