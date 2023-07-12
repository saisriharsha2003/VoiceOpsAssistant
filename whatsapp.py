import pywhatkit
import vobject

name = input()
with open('all contacts .vcf') as f:
    vcards = vobject.readComponents(f.read())
l = []
for vcard in vcards:
    if hasattr(vcard, 'fn') and vcard.fn.value.lower() == name.lower():
        if hasattr(vcard, 'tel') and vcard.tel:
            for p_no in vcard.contents['tel']:
                ph_no = str(p_no.value)
                l.append(ph_no)
phone_number = l[0]
if len(phone_number) < 13:
    phone_number = "+91" + phone_number
message = input()
pywhatkit.sendwhatmsg_instantly(phone_number, message)