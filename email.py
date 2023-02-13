import imaplib
import base64
email_user = "aaronwq32@outlook.com"
email_pass = "wjdwlsdn123"

M = imaplib.IMAP4_SSL('imap-mail.outlook.com', 993)
M.login(email_user, email_pass)
M.select()

days = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]
months = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]

typ, data = M.search(None, '(FROM "noreply@codementor.io")')
# typ, data = M.search(None, 'All')

hours_hist = [0] * 24
days_hist = [0] * 7
months_hist = [0] * 12

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

    if "noreply@codementor.io" not in date:
        continue

    print(f"------{num}/{total}-------\n")
    print(date)
            

    st = len(" Mon, 07 Feb 2022 ")
    ed = len(" Mon, 07 Feb 2022 18")
    h = int(date[st:ed])

    day = date[1:4]

    st1 = len(" Mon, 07 ")
    ed1 = len(" Mon, 07 Feb")
    month = date[st1:ed1]

    day_index = days.index(day)
    if day_index >= 0:
        days_hist[day_index] += 1

    month_index = months.index(month)
    if month_index >= 0:
        months_hist[month_index] += 1

    # print(subject)    
    hours_hist[h] += 1

    print("Date:        ", month, day, h)
    print("")
    print("Hours Hist", hours_hist)
    print("Days Hist", days_hist)
    print("Months Hist", months_hist)
    print("\n")


    # print('Message %s\n%s\n' % (num, data[0][1]))  # don't you want to print num1 and data1 here?

M.close()
M.logout()

# Hours Hist [631, 620, 584, 554, 496, 457, 430, 477, 384, 404, 513, 502, 541, 591, 712, 696, 779, 842, 885, 852, 819, 775, 781, 676]
# Days Hist [2433, 2359, 2476, 2371, 2152, 1494, 1716]
# Months Hist [0, 0, 0, 0, 0, 814, 2207, 2184, 2293, 2706, 2686, 2111]
