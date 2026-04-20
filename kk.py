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
    "244992204792", "244914299871", "244914219713", "244914216425",
    "244914252534", "244914346835", "244914163952", "244914175961",
    "244914283451", "244914164906", "244914218755", "244914174143",
    "244992336041", "244914228541", "244914159593", "244914337198",
    "244914344586", "244914162687", "244914339802", "244914284864",
    "244914198246", "244914200181", "244992400291", "244914559238",
    "244914258737", "244914280356", "244914063687", "244914219965",
    "244914392383", "244992231054", "244914228458", "244914260584",
    "244914162493", "244914177093", "244914305758", "244914186404",
    "244914586386", "244992356538", "244914189444", "244914208502",
    "244914113439", "244914339272", "244914208511", "244992441546",
    "244992007129", "244914357566", "244914138524", "244991595642",
    "244914189442", "244914197401", "244914495513", "244991483413",
    "244914302597", "244991587205", "244914165987", "244914188367",
    "244914227165", "244914262464", "244914288662", "244992246212",
    "244914249412", "244914203081", "244914340948", "244992356728",
    "244914662151", "244914215430", "244914194805", "244914221851",
    "244914244589", "244914249540", "244914086281", "244914349321",
    "244914265695", "244914245584", "244914298939", "244914150131",
    "244914569412", "244991530581", "244914233647", "244914181048",
    "244914047570", "244914208913", "244991464273", "244914299542",
    "244914269075", "244914649133", "244991927007", "244914206124",
    "244914365557", "244914280003", "244914161501", "244914040613",
    "244914152383", "244914158888", "244914485392", "244991485573",
    "244914413114", "244914333465", "244914554975", "244991819812",
    "244914231022", "244914339713", "244914141824", "244914215265",
    "244914160991", "244914221518", "244914345049", "244914181875",
    "244914183018", "244914262283", "244992128748", "244991945802",
    "244914262247", "244991521550", "244914206166", "244914219039",
    "244914342000", "244992462365", "244914252046", "244991429967",
    "244992159125", "244914155799", "244991493137", "244914059179",
    "244914252664", "244914194035", "244992388091", "244914358993",
    "244914292139", "244914185071", "244914188955", "244914171611",
    "244914178265", "244914185538", "244914290953", "244914245274",
    "244914260244", "244914266053", "244991888276", "244914155661",
    "244914288859", "244914345860", "244914225173", "244992299256",
    "244914218979", "244914181268", "244914219857", "244914151966",
    "244914330900", "244914225902", "244914044253", "244914175806",
    "244914118693", "244914223170", "244991430689", "244914246654",
    "244914249656", "244914231703", "244914175673", "244914262491",
    "244914644207", "244914495947", "244914160863", "244918580328",
    "244914184206", "244991456138", "244914178936", "244914187549",
    "244914351744", "244914149796", "244914227180", "244914340480",
    "244914204219", "244991521732", "244914234817", "244991623989",
    "244991704184", "244914181392", "244914232701", "244991692396",
    "244914160367", "244991440443", "244914262396", "244914152107",
    "244914118708", "244914157945", "244914200613", "244914588757",
    "244992103273", "244914295515", "244991493002", "244914247880",
    "244914227145", "244914216112", "244992335391", "244914642166",
    "244914282639", "244914189439", "244991963428", "244991782623",
    "244914344529", "244914337107", "244914240037", "244914513259",
    "244991592076", "244991455967", "244914249147", "244914301828",
    "244914243578", "244914185033", "244914173270", "244914189402",
    "244914182304", "244992330266", "244914338865", "244914176364",
    "244914252011", "244914183443", "244914159017", "244914343664",
    "244914256019", "244914202729", "244992361631", "244914609367",
    "244918572580", "244991613197", "244914249550", "244914295306",
    "244914188569", "244991764349", "244914629703", "244992078671",
    "244914221837", "244914298627", "244914348460", "244914216744",
    "244914344571", "244914351439", "244914291388", "244914333047",
    "244914337635", "244914487519", "244914199628", "244914292699",
    "244914225169", "244914161524", "244914215410", "244914064284",
    "244992005581", "244914492646", "244914266775", "244914226222",
    "244914214135", "244914235338", "244914211448", "244992091303",
    "244914216108", "244992379496", "244914281209", "244991845314",
    "244914169396", "244914107882", "244914205315", "244914385506",
    "244991976720", "244914559723", "244914286550", "244914210311",
    "244991770731", "244918558396", "244914356943", "244914354590",
    "244914205436", "244914347756", "244914231647", "244991623779",
    "244914171057", "244914029924", "244914281628", "244992461196",
    "244914154791", "244992415254", "244914120682", "244914182036",
    "244991851948", "244914285296", "244914295380", "244914245114",
    "244914203838", "244914352904", "244914303129", "244992012664",
    "244914201668", "244914568411", "244914295064", "244991522820",
    "244914040576", "244914166724", "244991589600", "244914185094",
    "244914246046", "244914198258", "244991926844", "244991960534",
    "244914285871", "244991777382", "244991693380", "244914229587",
    "244914550232", "244914188882", "244914226282", "244914334562",
    "244914662094", "244914283276", "244991535408", "244991929668",
    "244914173962", "244991553388", "244992465621", "244914194069",
    "244914285538", "244991615946", "244914216459", "244914222895",
    "244914355076", "244914040539", "244914092582", "244914185313",
    "244914301114", "244914157765", "244991694843", "244914172412",
    "244914482112", "244914373627", "244914333327", "244992152897",
    "244914194408", "244914225104", "244914438696", "244914027013",
    "244992162370", "244914236193", "244992002003", "244914185029",
    "244914338643", "244914139178", "244914226812", "244914216712",
    "244914336037", "244914342725", "244914247895", "244992347330",
    "244914206188", "244992343483", "244914203880", "244992192715",
    "244914258765", "244914197036", "244914216028", "244991448550",
    "244914177576", "244914150551", "244914358248", "244914165178",
    "244914345938", "244992155459", "244991533921", "244914183658",
    "244914298490", "244914191277", "244914356787", "244914243095",
    "244914198034", "244914194231", "244914299802", "244914176802",
    "244914168857", "244914124421", "244914362282", "244992123354",
    "244914154416", "244914537010", "244914216498", "244992050620",
    "244991918050", "244914183881", "244914567137", "244914179384",
    "244992239847", "244914266249", "244992452962", "244914182603",
    "244914255810", "244914259912", "244991732239", "244914299928",
    "244914238079", "244914290573", "244914186078", "244914330134",
    "244914148259", "244991811906", "244914355416"
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
    num_accounts = 2  # يمكنك تغيير هذا الرقم حسب حاجتك
    
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
