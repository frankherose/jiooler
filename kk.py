from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
from selenium.webdriver.common.keys import Keys
import threading
import random
import string

def generate_random_email():
    """توليد بريد إلكتروني عشوائي"""
    domains = ["gmail.com"]
    username_length = random.randint(8, 15)
    username = ''.join(random.choices(string.ascii_lowercase + string.digits, k=username_length))
    domain = random.choice(domains)
    return f"{username}@{domain}"

def generate_random_phone():
    """توليد رقم هاتف عشوائي (لأنجولا - الكود +244)"""
    # الكود: +244 + 9 أرقام عشوائية
    numbers = random.choice( [
    "255650319477", "255650682697", "255650326207", "255650311096",
    "255650226295", "255650324888", "255650321559", "255650222393",
    "255650749105", "255650759570", "255650192591", "255650751999",
    "255650763278", "255650188913", "255650762490", "255650222322",
    "255650760128", "255650229470", "255650777030", "255650758629",
    "255650318589", "255650218134", "255650234982", "255650746703",
    "255650308543", "255650236663", "255650313405", "255650195250",
    "255650227182", "255650229742", "255650759541", "255650752294",
    "255650750335", "255650749913", "255650748135", "255650747947",
    "255650696854", "255650697342", "255650287036", "255650237392",
    "255650234243", "255650221861", "255650757192", "255650203303",
    "255650757499", "255650219176", "255650193498", "255650296853",
    "255650771350", "255650771110", "255650307413", "255650707193",
    "255650746824", "255650248633", "255650230482", "255650680634",
    "255650786661", "255650751633", "255650679767", "255650749838",
    "255650707895", "255650679955", "255650705816", "255650757589",
    "255650723441", "255650222867", "255650230798", "255650194848",
    "255650773982", "255650325686", "255650204426", "255650310112",
    "255650679505", "255650197244", "255650780831", "255650293769",
    "255650202329", "255650231298", "255650307736", "255650202427",
    "255650307776", "255650205412", "255650212921", "255650683499",
    "255650774464", "255650225512", "255650760202", "255650229544",
    "255650758703", "255650218208", "255650746777", "255650189530",
    "255650308617", "255650774579", "255650236737", "255650751375",
    "255650750409", "255650749987", "255650750790", "255650748209",
    "255650748021", "255650287110", "255650221935", "255650756152",
    "255650757266", "255650307301", "255650221311", "255650320076",
    "255650296477", "255650193572", "255650296927", "255650771424",
    "255650771184", "255650749339", "255650230556", "255650317601",
    "255650786735", "255650786029", "255650770350", "255650229749",
    "255650679841", "255650680029", "255650306522", "255650746859",
    "255650776392", "255650194653", "255650705923", "255650194922",
    "255650325760", "255650204500", "255650282563", "255650679579",
    "255650191293", "255650228043", "255650252332", "255650202403",
    "255650247340", "255650191040", "255650759938", "255650208710",
    "255650325147", "255650741389", "255650231372", "255650210062",
    "255650234430", "255650712663", "255650324458", "255650738786",
    "255650323605", "255650307347", "255650212995", "255650238839",
    "255650785717", "255650786376", "255650756871", "255650192747",
    "255650266588", "255650778799", "255650295222", "255650680447",
    "255650750774", "255650237067", "255650195963", "255650318107",
    "255650745398", "255650199922", "255650222026", "255650218698",
    "255650209291", "255650324879", "255650223659", "255650226423",
    "255650783768", "255650749233", "255650192719", "255650785768",
    "255650732447", "255650189041", "255650771818", "255650225337",
    "255650307549", "255650226777", "255650232819", "255650760256",
    "255650755022", "255650758757", "255650766135", "255650189584",
    "255650308671", "255650215533", "255650774633", "255650227310",
    "255650229870", "255650750463", "255650748263", "255650292056",
    "255650238059", "255650234862", "255650756206", "255650757320",
    "255650281628", "255650734196", "255650221365", "255650757627",
    "255650714462", "255650219304", "255650296856", "255650771478",
    "255650324825", "255650702148", "255650307541", "255650311933",
    "255650749393", "255650781448", "255650746952", "255650287183",
    "255650230610", "255650680762", "255650786083", "255650679895",
    "255650276466", "255650749966", "255650302204", "255650327734",
    "255650693340", "255650746913", "255650221709", "255650700946",
    "255650776446", "255650785349", "255650757717", "255650697664",
    "255650194976", "255650774110", "255650329811", "255650325814",
    "255650204554", "255650679633", "255650748364", "255650191347",
    "255650780959", "255650197741", "255650191094", "255650780222",
    "255650309469", "255650208764", "255650325201", "255650286002",
    "255650191649", "255650308275", "255650231426", "255650210116",
    "255650234484", "255650324512", "255650307864", "255650307401",
    "255650205540", "255650774592", "255650711447", "255650225640",
    "255650285725", "255650316204", "255650756925", "255650210634",
    "255650228850", "255650680501", "255650221908", "255650750828",
    "255650204403", "255650205679", "255650237121", "255650279422",
    "255650196017", "255650785942", "255650271311", "255650222143",
    "255650204324", "255650223136", "255650207886", "255650218752",
    "255650210918", "255650189361", "255650324933", "255650223713",
    "255650265339", "255650282777", "255650326389", "255650222575",
    "255650749287", "255650192773", "255650230879", "255650189051",
    "255650762628", "255650679372", "255650775430", "255650225347",
    "255650230691", "255650701731", "255650229608", "255650719828",
    "255650697088", "255650778602", "255650218272", "255650235120",
    "255650766237", "255650766145", "255650195388", "255650759679",
    "255650750051", "255650748273", "255650748085", "255650699321",
    "255650234872", "255650221999", "255650784289", "255650757637",
    "255650304466", "255650290779", "255650211137", "255650296541",
    "255650193636", "255650771488", "255650771248", "255650307551",
    "255650781458", "255650746962", "255650786799", "255650751771",
    "255650229813", "255650719058", "255650190666", "255650680093",
    "255650704124", "255650302214", "255650723579", "255650223005",
    "255650194986", "255650732826", "255650204564", "255650748374",
    "255650191357", "255650780969", "255650293907", "255650191104",
    "255650780232", "255650779938", "255650208774", "255650325211",
    "255650272868", "255650231436", "255650323669", "255650307411",
    "255650225650", "255650786440", "255650327728", "255650756935",
    "255650192811", "255650778863", "255650228860", "255650680511",
    "255650308190", "255650196027", "255650249190", "255650318171",
    "255650271321", "255650222153", "255650266094", "255650204334",
    "255650199986", "255650222090", "255650207896", "255650270967",
    "255650249674", "255650209355", "255650189371", "255650223723",
    "255650310341", "255650259691", "255650682019", "255650326399",
    "255650209404", "255650222585", "255650759762", "255650192783",
    "255650240610", "255650706506", "255650785832", "255650230933",
    "255650763470", "255650189105", "255650779264", "255650323708",
    "255650762682", "255650771882", "255650301907", "255650230745",
    "255650307613", "255650222514", "255650232883", "255650760320",
    "255650229662", "255650760677", "255650265041", "255650755086",
    "255650758821", "255650766291", "255650746895", "255650766199",
    "255650189648", "255650195442", "255650229934", "255650751493",
    "255650750105", "255650748327", "255650748139", "255650292120",
    "255650290831", "255650757384", "255650203495", "255650221429",
    "255650757691", "255650290833", "255650211191", "255650219368",
    "255650193690", "255650324889", "255650307605", "255650747016",
    "255650323850", "255650230674", "255650712366", "255650786147",
    "255650688839", "255650313616", "255650770468", "255650229867",
    "255650679959", "255650750030", "255650190720", "255650680147",
    "255650302268", "255650327787", "255650220620", "255650723633",
    "255650223059", "255650230990", "255650687337", "255650325878",
    "255650748428", "255650191411", "255650197805", "255650731778",
    "255650198413", "255650702402", "255650202521", "255650191158",
    "255650780286", "255650779992", "255650208828", "255650308339",
    "255650210180", "255650681644", "255650324576", "255650738904",
    "255650205604", "255650327161", "255650698835", "255650268745",
    "255650774656", "255650711511", "255650225704", "255650316268",
    "255650756989", "255650192865", "255650211828", "255650778917",
    "255650295340", "255650240552", "255650204467", "255650276962",
    "255650291303", "255650279486", "255650214823", "255650308988",
    "255650310299", "255650296144", "255650222144", "255650223200",
    "255650207950", "255650247102", "255650189425", "255650324997",
    "255650278982", "255650754756", "255650203165", "255650307991",
    "255650226621", "255650774326", "255650227366", "255650750562"
])
    return f"+{numbers}"

def generate_random_password():
    """توليد كلمة مرور عشوائية قوية"""
    chars = string.ascii_letters + string.digits + "!@#$%^&*"
    password = ''.join(random.choices(chars, k=12))
    # التأكد من وجود حرف كبير وصغير ورقم ورمز
    if not any(c.isupper() for c in password):
        password += random.choice(string.ascii_uppercase)
    if not any(c.islower() for c in password):
        password += random.choice(string.ascii_lowercase)
    if not any(c.isdigit() for c in password):
        password += random.choice(string.digits)
    if not any(c in "!@#$%^&*" for c in password):
        password += random.choice("!@#$%^&*")
    return password

def create_account(account_number, results):
    """دالة لإنشاء حساب جديد باستخدام threading"""
    chrome_options = Options()
   # chrome_options.add_argument("--start-maximized")
    # إضافة خيارات لتسريع العملية وتقليل استهلاك الموارد
    chrome_options.add_argument("--disable-blink-features=AutomationControlled")
    chrome_options.add_experimental_option("excludeSwitches", ["enable-automation"])
    chrome_options.add_experimental_option('useAutomationExtension', False)
    chrome_options.add_argument('--lang=en')
    chrome_options.add_argument("--headless")
    driver = webdriver.Chrome(options=chrome_options)
    driver.set_page_load_timeout(190)  # زيادة إلى 120 ثانية
    driver.set_script_timeout(190)
    driver.implicitly_wait(30)
    try:
        print(f"🔄 [الحساب {account_number}] بدء عملية التسجيل...")
        
        # توليد بيانات عشوائية
        random_email = generate_random_email()
        random_phone = generate_random_phone()
        random_password = "Mmais123zx@#"
        
        print(f"📧 [الحساب {account_number}] البريد الإلكتروني: {random_email}")
        print(f"📱 [الحساب {account_number}] رقم الهاتف: {random_phone}")
        print(f"🔑 [الحساب {account_number}] كلمة المرور: {random_password}")
        
        # ========== فتح صفحة التسجيل ==========
        url = "https://fantasino.com/registration?step=1&type=email"
        driver.get(url)
        print(f"✅ [الحساب {account_number}] تم فتح صفحة التسجيل")
        
        wait = WebDriverWait(driver, 15)
        
        # ملء البريد الإلكتروني
        email_field = wait.until(EC.element_to_be_clickable((By.ID, "email")))
        email_field.clear()
        email_field.send_keys(random_email)
        print(f"✅ [الحساب {account_number}] تم ملء البريد")
        
        # ملء رقم الهاتف
        phone_field = wait.until(EC.presence_of_element_located((By.ID, "phone")))
        driver.execute_script("arguments[0].scrollIntoView(true);", phone_field)
        #time.sleep(0.5)
        
        phone_field = wait.until(EC.element_to_be_clickable((By.ID, "phone")))
        driver.execute_script("arguments[0].value = '';", phone_field)
       #time.sleep(0.3)
        phone_field.send_keys(Keys.CONTROL + "a")
        #phone_field.send_keys(Keys.DELETE)
        #time.sleep(0.6)
        phone_field.send_keys(random_phone)
        print(f"✅ [الحساب {account_number}] تم ملء رقم الهاتف")
        
        # ملء كلمة المرور
        password_field = wait.until(EC.element_to_be_clickable((By.ID, "password")))
        password_field.clear()
        password_field.send_keys(random_password)
        print(f"✅ [الحساب {account_number}] تم ملء كلمة المرور")
        
        # تمرير الصفحة إلى أسفل
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        #time.sleep(1)
        
        # تحديد مربع الاشتراك
        subscribed_checkbox = wait.until(EC.presence_of_element_located((By.ID, "subscribed")))
        if not subscribed_checkbox.is_selected():
            driver.execute_script("arguments[0].click();", subscribed_checkbox)
            print(f"✅ [الحساب {account_number}] تم تحديد مربع الاشتراك")
        
        # تحديد مربع الشروط
        terms_checkbox = wait.until(EC.presence_of_element_located((By.ID, "terms")))
        if not terms_checkbox.is_selected():
            driver.execute_script("arguments[0].click();", terms_checkbox)
            print(f"✅ [الحساب {account_number}] تم تحديد مربع الشروط")
        
        # الضغط على زر Finish
        finish_button = wait.until(EC.element_to_be_clickable((By.XPATH, "//button[text()='Finish']")))
        driver.execute_script("arguments[0].scrollIntoView(true);", finish_button)
        #time.sleep(0.5)
        driver.execute_script("arguments[0].click();", finish_button)
        print(f"✅ [الحساب {account_number}] تم الضغط على زر Finish")
        
        # انتظار اكتمال عملية التسجيل
        time.sleep(5)
        
        # ========== الانتقال إلى صفحة الملف الشخصي ==========
        profile_url = "https://fantasino.com/account/profile/info"
        driver.get(profile_url)
        print(f"✅ [الحساب {account_number}] تم الانتقال إلى صفحة الملف الشخصي")
        
        time.sleep(0.1)
        
        # ========== الضغط على "Verify your number" ==========
        try:
            verify_number_element = wait.until(EC.element_to_be_clickable((By.XPATH, "//span[text()='Verify your number']")))
            driver.execute_script("arguments[0].scrollIntoView(true);", verify_number_element)
            #time.sleep(0.5)
            driver.execute_script("arguments[0].click();", verify_number_element)
            print(f"✅ [الحساب {account_number}] تم الضغط على 'Verify your number'")
            
            time.sleep(0.1)
            
            # ========== الضغط على زر Verify ==========
            verify_button = wait.until(EC.element_to_be_clickable((By.XPATH, "//button[text()='Verify']")))
            driver.execute_script("arguments[0].scrollIntoView(true);", verify_button)
           # time.sleep(0.5)
            driver.execute_script("arguments[0].click();", verify_button)
            print(f"✅ [الحساب {account_number}] تم الضغط على زر Verify")
            
            # حفظ بيانات الحساب الناجح
            results.append({
                "account_number": account_number,
                "email": random_email,
                "phone": random_phone,
                "password": random_password,
                "status": "success"
            })
            
            time.sleep(3)
            
        except Exception as e:
            print(f"❌ [الحساب {account_number}] خطأ في عملية التحقق: {e}")
            results.append({
                "account_number": account_number,
                "email": random_email,
                "phone": random_phone,
                "password": random_password,
                "status": "verification_failed",
                "error": str(e)
            })
        
        
        wait = WebDriverWait(driver, 70)
        button = wait.until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, "p.ui-typography.ui-typography_size_lg.ui-typography_kind_brand-color-3-500"))
    )
        button.click()
        print("تم الضغط على الزر بنجاح")
        print(f"✅ [الحساب {account_number}] اكتملت العملية بنجاح")

        time.sleep(4)
        
    except Exception as e:
        print(f"❌ [الحساب {account_number}] حدث خطأ عام: {e}")
        results.append({
            "account_number": account_number,
            "status": "failed",
            "error": str(e)
        })
        driver.save_screenshot(f"error_screenshot_account_{account_number}.png")
        
    finally:
        driver.quit()
        print(f"🔒 [الحساب {account_number}] تم إغلاق المتصفح")
        create_account(999,results)

def main():
    """الدالة الرئيسية لتشغيل عدة حسابات بشكل متوازي"""
    
    print("=" * 60)
    print("🚀 بدء تشغيل نظام إنشاء الحسابات المتعدد")
    print("=" * 60)
    
    # تحديد عدد الحسابات المطلوب إنشاؤها
    num_accounts = 4  # يمكنك تغيير هذا الرقم حسب حاجتك
    
    print(f"📊 عدد الحسابات المطلوب إنشاؤها: {num_accounts}")
    print("=" * 60)
    
    results = []
    threads = []
    
    # إنشاء وتشغيل الخيوط
    for i in range(1, num_accounts + 1):
        thread = threading.Thread(target=create_account, args=(i, results))
        threads.append(thread)
        thread.start()
        
        # انتظار قليلاً بين بدء الخيوط لتجنب التحميل الزائد
        time.sleep(1.111)
    
    # انتظار اكتمال جميع الخيوط
    for thread in threads:
        thread.join()
    
    # عرض النتائج النهائية
    print("\n" + "=" * 60)
    print("📊 تقرير النتائج النهائي")
    print("=" * 60)
    
    successful = [r for r in results if r.get('status') == 'success']
    failed = [r for r in results if r.get('status') != 'success']
    
    print(f"✅ الحسابات الناجحة: {len(successful)}")
    print(f"❌ الحسابات الفاشلة: {len(failed)}")
    
    if successful:
        print("\n📝 تفاصيل الحسابات الناجحة:")
        for account in successful:
            print(f"  الحساب {account['account_number']}:")
            print(f"    📧 البريد: {account['email']}")
            print(f"    📱 الهاتف: {account['phone']}")
            print(f"    🔑 كلمة المرور: {account['password']}")
            print("-" * 40)
    
    if failed:
        print("\n⚠️ الحسابات الفاشلة:")
        for account in failed:
            print(f"  الحساب {account['account_number']}: {account.get('error', 'خطأ غير معروف')}")
    
    print("\n✨ تم الانتهاء من إنشاء جميع الحسابات")

while True:
    main()
