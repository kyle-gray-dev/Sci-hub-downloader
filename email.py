import imaplib
import base64
email_user = "yuetongyang@outlook.com"
email_pass = "wjdwlsdn123"

M = imaplib.IMAP4_SSL('imap-mail.outlook.com', 993)
M.login(email_user, email_pass)
M.select()

typ, data = M.search(None, 'ALL')

hist = [0] * 24

total = len(data[0].split())
for num in data[0].split():
    typ, data = M.fetch(num, '(RFC822)')   # data is being redefined here, that's probably not right
    content = data[0][1].decode()

    # pos1 = content.find("Subject:")
    # pos2 = content.find("Thread-Topic:")

    pos3 = content.find("Date:")
    pos4 = content.find("Message-ID:")

    if pos3 < 0 or pos4 < 0:
        continue

    # pos1 += len("Subject:")
    pos3 += len("Date:")

    # subject = content[pos1:pos2]
    date = content[pos3:pos4]

    if "notifications@codementor.io" not in date:
        continue

    st = len(" Mon, 07 Feb 2022 ")
    ed = len(" Mon, 07 Feb 2022 18")
    h = int(date[st:ed])

    # print(subject)
    print(f"------{num}/{total}-------\n")
    print(date)
    hist[h] += 1

    print("Hours", str(h))
    print("")
    print("Hist", hist)
    print("\n")


    # print('Message %s\n%s\n' % (num, data[0][1]))  # don't you want to print num1 and data1 here?

M.close()
M.logout()