# Generated by Django 4.2 on 2024-04-10 10:35

from django.conf import settings
import django.contrib.auth.models
import django.contrib.auth.validators
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone
import phonenumber_field.modelfields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserDatas',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('username', models.CharField(error_messages={'unique': 'A user with that username already exists.'}, help_text='Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.', max_length=150, unique=True, validators=[django.contrib.auth.validators.UnicodeUsernameValidator()], verbose_name='username')),
                ('first_name', models.CharField(blank=True, max_length=150, verbose_name='first name')),
                ('last_name', models.CharField(blank=True, max_length=150, verbose_name='last name')),
                ('is_staff', models.BooleanField(default=False, help_text='Designates whether the user can log into this admin site.', verbose_name='staff status')),
                ('is_active', models.BooleanField(default=True, help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.', verbose_name='active')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined')),
                ('email', models.EmailField(max_length=50, validators=[django.core.validators.EmailValidator(message='enter valid email')])),
                ('password', models.CharField(max_length=300, validators=[django.core.validators.MinLengthValidator(4)])),
                ('confirm_password', models.CharField(max_length=300)),
                ('role', models.CharField(choices=[('Player', 'Player'), ('Coach', 'Coach'), ('Ground Owner', 'Ground Owner')], max_length=20)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.permission', verbose_name='user permissions')),
            ],
            options={
                'verbose_name': 'user',
                'verbose_name_plural': 'users',
                'abstract': False,
            },
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.CreateModel(
            name='Profiles',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=50)),
                ('birthdate', models.DateField()),
                ('gender', models.CharField(choices=[('MALE', 'MALE'), ('FEMALE', 'FEMALE'), ('OTHERS', 'OTHERS')], max_length=10)),
                ('nationality', models.CharField(choices=[('AF', 'Afghanistan'), ('AX', 'Åland Islands'), ('AL', 'Albania'), ('DZ', 'Algeria'), ('AS', 'American Samoa'), ('AD', 'Andorra'), ('AO', 'Angola'), ('AI', 'Anguilla'), ('AQ', 'Antarctica'), ('AG', 'Antigua and Barbuda'), ('AR', 'Argentina'), ('AM', 'Armenia'), ('AW', 'Aruba'), ('AU', 'Australia'), ('AT', 'Austria'), ('AZ', 'Azerbaijan'), ('BS', 'Bahamas'), ('BH', 'Bahrain'), ('BD', 'Bangladesh'), ('BB', 'Barbados'), ('BY', 'Belarus'), ('BE', 'Belgium'), ('BZ', 'Belize'), ('BJ', 'Benin'), ('BM', 'Bermuda'), ('BT', 'Bhutan'), ('BO', 'Bolivia'), ('BQ', 'Bonaire, Sint Eustatius and Saba'), ('BA', 'Bosnia and Herzegovina'), ('BW', 'Botswana'), ('BV', 'Bouvet Island'), ('BR', 'Brazil'), ('IO', 'British Indian Ocean Territory'), ('BN', 'Brunei'), ('BG', 'Bulgaria'), ('BF', 'Burkina Faso'), ('BI', 'Burundi'), ('CV', 'Cabo Verde'), ('KH', 'Cambodia'), ('CM', 'Cameroon'), ('CA', 'Canada'), ('KY', 'Cayman Islands'), ('CF', 'Central African Republic'), ('TD', 'Chad'), ('CL', 'Chile'), ('CN', 'China'), ('CX', 'Christmas Island'), ('CC', 'Cocos (Keeling) Islands'), ('CO', 'Colombia'), ('KM', 'Comoros'), ('CG', 'Congo'), ('CD', 'Congo (the Democratic Republic of the)'), ('CK', 'Cook Islands'), ('CR', 'Costa Rica'), ('CI', "Côte d'Ivoire"), ('HR', 'Croatia'), ('CU', 'Cuba'), ('CW', 'Curaçao'), ('CY', 'Cyprus'), ('CZ', 'Czechia'), ('DK', 'Denmark'), ('DJ', 'Djibouti'), ('DM', 'Dominica'), ('DO', 'Dominican Republic'), ('EC', 'Ecuador'), ('EG', 'Egypt'), ('SV', 'El Salvador'), ('GQ', 'Equatorial Guinea'), ('ER', 'Eritrea'), ('EE', 'Estonia'), ('SZ', 'Eswatini'), ('ET', 'Ethiopia'), ('FK', 'Falkland Islands (Malvinas)'), ('FO', 'Faroe Islands'), ('FJ', 'Fiji'), ('FI', 'Finland'), ('FR', 'France'), ('GF', 'French Guiana'), ('PF', 'French Polynesia'), ('TF', 'French Southern Territories'), ('GA', 'Gabon'), ('GM', 'Gambia'), ('GE', 'Georgia'), ('DE', 'Germany'), ('GH', 'Ghana'), ('GI', 'Gibraltar'), ('GR', 'Greece'), ('GL', 'Greenland'), ('GD', 'Grenada'), ('GP', 'Guadeloupe'), ('GU', 'Guam'), ('GT', 'Guatemala'), ('GG', 'Guernsey'), ('GN', 'Guinea'), ('GW', 'Guinea-Bissau'), ('GY', 'Guyana'), ('HT', 'Haiti'), ('HM', 'Heard Island and McDonald Islands'), ('VA', 'Holy See'), ('HN', 'Honduras'), ('HK', 'Hong Kong'), ('HU', 'Hungary'), ('IS', 'Iceland'), ('IN', 'India'), ('ID', 'Indonesia'), ('IR', 'Iran'), ('IQ', 'Iraq'), ('IE', 'Ireland'), ('IM', 'Isle of Man'), ('IL', 'Israel'), ('IT', 'Italy'), ('JM', 'Jamaica'), ('JP', 'Japan'), ('JE', 'Jersey'), ('JO', 'Jordan'), ('KZ', 'Kazakhstan'), ('KE', 'Kenya'), ('KI', 'Kiribati'), ('KW', 'Kuwait'), ('KG', 'Kyrgyzstan'), ('LA', 'Laos'), ('LV', 'Latvia'), ('LB', 'Lebanon'), ('LS', 'Lesotho'), ('LR', 'Liberia'), ('LY', 'Libya'), ('LI', 'Liechtenstein'), ('LT', 'Lithuania'), ('LU', 'Luxembourg'), ('MO', 'Macao'), ('MG', 'Madagascar'), ('MW', 'Malawi'), ('MY', 'Malaysia'), ('MV', 'Maldives'), ('ML', 'Mali'), ('MT', 'Malta'), ('MH', 'Marshall Islands'), ('MQ', 'Martinique'), ('MR', 'Mauritania'), ('MU', 'Mauritius'), ('YT', 'Mayotte'), ('MX', 'Mexico'), ('FM', 'Micronesia (Federated States of)'), ('MD', 'Moldova'), ('MC', 'Monaco'), ('MN', 'Mongolia'), ('ME', 'Montenegro'), ('MS', 'Montserrat'), ('MA', 'Morocco'), ('MZ', 'Mozambique'), ('MM', 'Myanmar'), ('NA', 'Namibia'), ('NR', 'Nauru'), ('NP', 'Nepal'), ('NL', 'Netherlands'), ('NC', 'New Caledonia'), ('NZ', 'New Zealand'), ('NI', 'Nicaragua'), ('NE', 'Niger'), ('NG', 'Nigeria'), ('NU', 'Niue'), ('NF', 'Norfolk Island'), ('KP', 'North Korea'), ('MK', 'North Macedonia'), ('MP', 'Northern Mariana Islands'), ('NO', 'Norway'), ('OM', 'Oman'), ('PK', 'Pakistan'), ('PW', 'Palau'), ('PS', 'Palestine, State of'), ('PA', 'Panama'), ('PG', 'Papua New Guinea'), ('PY', 'Paraguay'), ('PE', 'Peru'), ('PH', 'Philippines'), ('PN', 'Pitcairn'), ('PL', 'Poland'), ('PT', 'Portugal'), ('PR', 'Puerto Rico'), ('QA', 'Qatar'), ('RE', 'Réunion'), ('RO', 'Romania'), ('RU', 'Russia'), ('RW', 'Rwanda'), ('BL', 'Saint Barthélemy'), ('SH', 'Saint Helena, Ascension and Tristan da Cunha'), ('KN', 'Saint Kitts and Nevis'), ('LC', 'Saint Lucia'), ('MF', 'Saint Martin (French part)'), ('PM', 'Saint Pierre and Miquelon'), ('VC', 'Saint Vincent and the Grenadines'), ('WS', 'Samoa'), ('SM', 'San Marino'), ('ST', 'Sao Tome and Principe'), ('SA', 'Saudi Arabia'), ('SN', 'Senegal'), ('RS', 'Serbia'), ('SC', 'Seychelles'), ('SL', 'Sierra Leone'), ('SG', 'Singapore'), ('SX', 'Sint Maarten (Dutch part)'), ('SK', 'Slovakia'), ('SI', 'Slovenia'), ('SB', 'Solomon Islands'), ('SO', 'Somalia'), ('ZA', 'South Africa'), ('GS', 'South Georgia and the South Sandwich Islands'), ('KR', 'South Korea'), ('SS', 'South Sudan'), ('ES', 'Spain'), ('LK', 'Sri Lanka'), ('SD', 'Sudan'), ('SR', 'Suriname'), ('SJ', 'Svalbard and Jan Mayen'), ('SE', 'Sweden'), ('CH', 'Switzerland'), ('SY', 'Syria'), ('TW', 'Taiwan'), ('TJ', 'Tajikistan'), ('TZ', 'Tanzania'), ('TH', 'Thailand'), ('TL', 'Timor-Leste'), ('TG', 'Togo'), ('TK', 'Tokelau'), ('TO', 'Tonga'), ('TT', 'Trinidad and Tobago'), ('TN', 'Tunisia'), ('TR', 'Türkiye'), ('TM', 'Turkmenistan'), ('TC', 'Turks and Caicos Islands'), ('TV', 'Tuvalu'), ('UG', 'Uganda'), ('UA', 'Ukraine'), ('AE', 'United Arab Emirates'), ('GB', 'United Kingdom'), ('UM', 'United States Minor Outlying Islands'), ('US', 'United States of America'), ('UY', 'Uruguay'), ('UZ', 'Uzbekistan'), ('VU', 'Vanuatu'), ('VE', 'Venezuela'), ('VN', 'Vietnam'), ('VG', 'Virgin Islands (British)'), ('VI', 'Virgin Islands (U.S.)'), ('WF', 'Wallis and Futuna'), ('EH', 'Western Sahara'), ('YE', 'Yemen'), ('ZM', 'Zambia'), ('ZW', 'Zimbabwe'), ('', 'Select Country')], max_length=200)),
                ('phone', phonenumber_field.modelfields.PhoneNumberField(max_length=128, region=None)),
                ('profile_pic', models.ImageField(blank=True, null=True, upload_to='static/upload_images/')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('user_data_id', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Players',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('aita_ranking', models.IntegerField(blank=True, null=True)),
                ('skills', models.CharField(choices=[('RECREATION', 'RECREATION'), ('BASIC', 'BASIC'), ('INTERMEDIATE', 'INTERMEDIATE'), ('EXPERT', 'EXPERT')], max_length=20)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('player_profile_id', models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='player', to='SportingBuddiesApp.profiles')),
            ],
        ),
        migrations.CreateModel(
            name='GroundProviders',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('ground_name', models.CharField(max_length=50)),
                ('ammenities', models.TextField()),
                ('facilities', models.TextField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('ground_provider_profile_id', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='SportingBuddiesApp.profiles')),
            ],
        ),
        migrations.CreateModel(
            name='CourtDetails',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('court_name', models.CharField(max_length=50)),
                ('surface_type', models.CharField(choices=[('Sandy Soil', 'Sandy Soil'), ('Silt Soil', 'Silt Soil'), ('Clay Soil', 'Clay Soil')], max_length=20)),
                ('price', models.IntegerField()),
                ('light_availability', models.BooleanField(default=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('ground_datas_ids', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='SportingBuddiesApp.groundproviders')),
            ],
        ),
        migrations.CreateModel(
            name='Coaches',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('qualification', models.CharField(max_length=50)),
                ('certificate', models.TextField(blank=True, null=True)),
                ('prices', models.IntegerField()),
                ('technique', models.CharField(max_length=50)),
                ('specialities', models.CharField(choices=[('RECREATION', 'RECREATION'), ('BASIC', 'BASIC'), ('INTERMEDIATE', 'INTERMEDIATE'), ('EXPERT', 'EXPERT')], max_length=15, null=True)),
                ('experience', models.IntegerField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('coaches_profile_id', models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='coach', to='SportingBuddiesApp.profiles')),
            ],
        ),
        migrations.CreateModel(
            name='Addresses',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('flat_no', models.CharField(max_length=5)),
                ('landmark', models.TextField()),
                ('area', models.TextField()),
                ('city', models.CharField(blank=True, choices=[('Andaman and Nicobar Islands', (('Port Blair', 'Port Blair'),)), ('Andhra Pradesh', (('Visakhapatnam', 'Visakhapatnam'), ('Vijayawada', 'Vijayawada'), ('Guntur', 'Guntur'), ('Nellore', 'Nellore'), ('Kurnool', 'Kurnool'), ('Rajamahendravaram', 'Rajamahendravaram'), ('Tirupati', 'Tirupati'), ('Kadapa', 'Kadapa'), ('Kakinada', 'Kakinada'), ('Anantapur', 'Anantapur'), ('Vizianagaram', 'Vizianagaram'), ('Eluru', 'Eluru'), ('Ongole', 'Ongole'), ('Nandyal', 'Nandyal'), ('Machilipatnam', 'Machilipatnam'), ('Adoni', 'Adoni'), ('Tenali', 'Tenali'), ('Proddatur', 'Proddatur'), ('Chittoor', 'Chittoor'), ('Hindupur', 'Hindupur'), ('Bhimavaram', 'Bhimavaram'), ('Madanapalle', 'Madanapalle'), ('Guntakal', 'Guntakal'), ('Srikakulam', 'Srikakulam'), ('Dharmavaram', 'Dharmavaram'), ('Gudivada', 'Gudivada'), ('Narasaraopet', 'Narasaraopet'), ('Tadipatri', 'Tadipatri'), ('Tadepalligudem', 'Tadepalligudem'), ('Amaravati', 'Amaravati'), ('Chilakaluripet', 'Chilakaluripet'))), ('Arunachal Pradesh', (('Itanagar', 'Itanagar'),)), ('Assam', (('Dhuburi', 'Dhuburi'), ('Dibrugarh', 'Dibrugarh'), ('Dispur', 'Dispur'), ('Guwahati', 'Guwahati'), ('Jorhat', 'Jorhat'), ('Nagaon', 'Nagaon'), ('Sivasagar', 'Sivasagar'), ('Silchar', 'Silchar'), ('Tezpur', 'Tezpur'), ('Tinsukia', 'Tinsukia'))), ('Bihar', (('Patna', 'Patna'), ('Gaya', 'Gaya'), ('Bhagalpur', 'Bhagalpur'), ('Muzaffarpur', 'Muzaffarpur'), ('Purnia', 'Purnia'), ('Darbhanga', 'Darbhanga'), ('Bihar Sharif', 'Bihar Sharif'), ('Arrah', 'Arrah'), ('Begusarai', 'Begusarai'), ('Katihar', 'Katihar'), ('Munger', 'Munger'), ('Chhapra', 'Chhapra'), ('Bettiah', 'Bettiah'), ('Saharsa', 'Saharsa'), ('Hajipur', 'Hajipur'), ('Sasaram', 'Sasaram'), ('Dehri', 'Dehri'), ('Siwan', 'Siwan'), ('Motihari', 'Motihari'), ('Nawada', 'Nawada'), ('Bagaha', 'Bagaha'), ('Buxar', 'Buxar'), ('Kishanganj', 'Kishanganj'), ('Sitamarhi', 'Sitamarhi'), ('Jamalpur', 'Jamalpur'), ('Jehanabad', 'Jehanabad'), ('Aurangabad', 'Aurangabad'), ('Lakhisarai', 'Lakhisarai'))), ('Chandigarh', (('Chandigarh', 'Chandigarh'),)), ('Chhattisgarh', (('Raipur', 'Raipur'), ('Durg', 'Durg'), ('Naya Raipur', 'Naya Raipur'), ('Korba', 'Korba'), ('Bilaspur', 'Bilaspur'), ('Rajnandgaon', 'Rajnandgaon'), ('Pakhanjore', 'Pakhanjore'), ('Jagdalpur', 'Jagdalpur'), ('Ambikapur', 'Ambikapur'), ('Chirmiri', 'Chirmiri'), ('Dhamtari', 'Dhamtari'), ('Raigarh', 'Raigarh'), ('Mahasamund', 'Mahasamund'))), ('Daman and Diu', (('Daman', 'Daman'),)), ('Delhi', (('Delhi', 'Delhi'),)), ('Dadra and Nagar Haveli', (('Silvassa', 'Silvassa'),)), ('Goa', (('Panaji', 'Panaji'), ('Vasco', 'Vasco'), ('Mormugao', 'Mormugao'), ('Margao', 'Margao'))), ('Gujarat', (('Ahmedabad', 'Ahmedabad'), ('Surat', 'Surat'), ('Vadodara', 'Vadodara'), ('Rajkot', 'Rajkot'), ('Bhavnagar', 'Bhavnagar'), ('Jamnagar', 'Jamnagar'), ('Junagadh', 'Junagadh'), ('Gandhidham', 'Gandhidham'), ('Nadiad', 'Nadiad'), ('Gandhinagar', 'Gandhinagar'), ('Anand', 'Anand'), ('Morbi', 'Morbi'), ('Khambhat', 'Khambhat'), ('Surendranagar', 'Surendranagar'), ('Bharuch', 'Bharuch'), ('Vapi', 'Vapi'), ('Navsari', 'Navsari'), ('Veraval', 'Veraval'), ('Porbandar', 'Porbandar'), ('Godhra', 'Godhra'), ('Bhuj', 'Bhuj'), ('Ankleshwar', 'Ankleshwar'), ('Botad', 'Botad'), ('Patan', 'Patan'), ('Palanpur', 'Palanpur'), ('Dahod', 'Dahod'), ('Jetpur', 'Jetpur'), ('Valsad', 'Valsad'), ('Kalol', 'Kalol'), ('Gondal', 'Gondal'), ('Deesa', 'Deesa'), ('Amreli', 'Amreli'), ('Amreli', 'Amreli'), ('Mahuva', 'Mahuva'), ('Mehsana', 'Mehsana'))), ('Himachal Pradesh', (('Shimla', 'Shimla'),)), ('Haryana', (('Faridabad', 'Faridabad'), ('Gurgaon', 'Gurgaon'), ('Panipat', 'Panipat'), ('Ambala', 'Ambala'), ('Yamunanagar', 'Yamunanagar'), ('Rohtak', 'Rohtak'), ('Hisar', 'Hisar'), ('Karnal', 'Karnal'), ('Sonipat', 'Sonipat'), ('Panchkula', 'Panchkula'), ('Bhiwani', 'Bhiwani'), ('Sirsa', 'Sirsa'), ('Bahadurgarh', 'Bahadurgarh'), ('Jind', 'Jind'), ('Thanesar', 'Thanesar'), ('Kaithal', 'Kaithal'), ('Rewari', 'Rewari'), ('Palwal', 'Palwal'))), ('Jharkhand', (('Jamshedpur', 'Jamshedpur'), ('Dhanbad', 'Dhanbad'), ('Ranchi', 'Ranchi'), ('Bokaro Steel City', 'Bokaro Steel City'), ('Deoghar', 'Deoghar'), ('Phusro', 'Phusro'), ('Hazaribagh', 'Hazaribagh'), ('Giridih', 'Giridih'), ('Ramgarh', 'Ramgarh'), ('Medininagar', 'Medininagar'), ('Chirkunda', 'Chirkunda'), ('Jhumri Telaiya', 'Jhumri Telaiya'), ('Sahibganj', 'Sahibganj'))), ('Jammu and Kashmir', (('Srinagar', 'Srinagar'), ('Jammu', 'Jammu'), ('Anantnag', 'Anantnag'))), ('Karnataka', (('Bengaluru', 'Bengaluru'), ('Hubli', 'Hubli'), ('Mysore', 'Mysore'), ('Gulbarga', 'Gulbarga'), ('Mangalore', 'Mangalore'), ('Belgaum', 'Belgaum'), ('Davangere', 'Davangere'), ('Bellary', 'Bellary'), ('Bijapur', 'Bijapur'), ('Shimoga', 'Shimoga'), ('Tumkur', 'Tumkur'), ('Raichur', 'Raichur'), ('Bidar', 'Bidar'), ('Hospet', 'Hospet'), ('Hassan', 'Hassan'), ('Gadag', 'Gadag'), ('Udupi', 'Udupi'), ('Robertsonpet', 'Robertsonpet'), ('Bhadravati', 'Bhadravati'), ('Chitradurga', 'Chitradurga'), ('Harihar', 'Harihar'), ('Kolar', 'Kolar'), ('Mandya', 'Mandya'), ('Chikkamagallooru', 'Chikkamagallooru'), ('Chikmagalur', 'Chikmagalur'), ('Gangawati', 'Gangawati'), ('Ranebennuru', 'Ranebennuru'), ('Ramanagara', 'Ramanagara'), ('Bagalkot', 'Bagalkot'))), ('Kerala', (('Thiruvananthapuram', 'Thiruvananthapuram'), ('Kochi', 'Kochi'), ('Calicut', 'Calicut'), ('Kollam', 'Kollam'), ('Thrissur', 'Thrissur'), ('Kannur', 'Kannur'), ('Kasaragod', 'Kasaragod'), ('Alappuzha', 'Alappuzha'), ('Alappuzha', 'Alappuzha'), ('Palakkad', 'Palakkad'), ('Kottayam', 'Kottayam'), ('Kothamangalam', 'Kothamangalam'), ('Malappuram', 'Malappuram'), ('Manjeri', 'Manjeri'), ('Thalassery', 'Thalassery'), ('Ponnani', 'Ponnani'))), ('Lakshadweep', (('Kavaratti', 'Kavaratti'),)), ('Maharashtra', (('Mumbai', 'Mumbai'), ('Pune', 'Pune'), ('Nagpur', 'Nagpur'), ('Nashik', 'Nashik'), ('Pimpri-Chinchwad', 'Pimpri-Chinchwad'), ('Aurangabad', 'Aurangabad'), ('Solapur', 'Solapur'), ('Bhiwandi', 'Bhiwandi'), ('Amravati', 'Amravati'), ('Nanded', 'Nanded'), ('Kolhapur', 'Kolhapur'), ('Sangli-Miraj-Kupwad', 'Sangli-Miraj-Kupwad'), ('Jalgaon', 'Jalgaon'), ('Akola', 'Akola'), ('Latur', 'Latur'), ('Malegaon', 'Malegaon'), ('Dhule', 'Dhule'), ('Ahmednagar', 'Ahmednagar'), ('Nandurbar', 'Nandurbar'), ('Ichalkaranji', 'Ichalkaranji'), ('Chandrapur', 'Chandrapur'), ('Jalna', 'Jalna'), ('Parbhani', 'Parbhani'), ('Bhusawal', 'Bhusawal'), ('Satara', 'Satara'), ('Beed', 'Beed'), ('Pandharpur', 'Pandharpur'), ('Yavatmal', 'Yavatmal'), ('Kamptee', 'Kamptee'), ('Gondia', 'Gondia'), ('Achalpur', 'Achalpur'), ('Osmanabad', 'Osmanabad'), ('Hinganghat', 'Hinganghat'), ('Wardha', 'Wardha'), ('Barshi', 'Barshi'), ('Chalisgaon', 'Chalisgaon'), ('Amalner', 'Amalner'), ('Khamgaon', 'Khamgaon'), ('Akot', 'Akot'), ('Udgir', 'Udgir'), ('Bhandara', 'Bhandara'), ('Parli', 'Parli'))), ('Meghalaya', (('Shillong', 'Shillong'),)), ('Manipur', (('Imphal', 'Imphal'),)), ('Madhya Pradesh', (('Indore', 'Indore'), ('Bhopal', 'Bhopal'), ('Jabalpur', 'Jabalpur'), ('Gwalior', 'Gwalior'), ('Ujjain', 'Ujjain'), ('Sagar', 'Sagar'), ('Dewas', 'Dewas'), ('Satna', 'Satna'), ('Ratlam', 'Ratlam'), ('Rewa', 'Rewa'), ('Katni', 'Katni'), ('Singrauli', 'Singrauli'), ('Burhanpur', 'Burhanpur'), ('Khandwa', 'Khandwa'), ('Morena', 'Morena'), ('Bhind', 'Bhind'), ('Chhindwara', 'Chhindwara'), ('Guna', 'Guna'), ('Shivpuri', 'Shivpuri'), ('Vidisha', 'Vidisha'), ('Chhatarpur', 'Chhatarpur'), ('Damoh', 'Damoh'), ('Mandsaur', 'Mandsaur'), ('Khargone', 'Khargone'), ('Neemuch', 'Neemuch'), ('Pithampur', 'Pithampur'), ('Hoshangabad', 'Hoshangabad'), ('Itarsi', 'Itarsi'), ('Sehore', 'Sehore'), ('Betul', 'Betul'), ('Seoni', 'Seoni'), ('Datia', 'Datia'), ('Nagda', 'Nagda'), ('Dhanpuri', 'Dhanpuri'), ('Dhar', 'Dhar'), ('Balaghat', 'Balaghat'))), ('Mizoram', (('Aizawl', 'Aizawl'),)), ('Nagaland', (('Dimapur', 'Dimapur'), ('Kohima', 'Kohima'))), ('Odisha', (('Bhubaneswar', 'Bhubaneswar'), ('Cuttack', 'Cuttack'), ('Rourkela', 'Rourkela'), ('Berhampur', 'Berhampur'), ('Sambalpur', 'Sambalpur'), ('Puri', 'Puri'), ('Balasore', 'Balasore'), ('Bhadrak', 'Bhadrak'), ('Baripada', 'Baripada'), ('Balangir', 'Balangir'), ('Jharsuguda', 'Jharsuguda'), ('Jeypore', 'Jeypore'))), ('Punjab', (('Ludhiana', 'Ludhiana'), ('Amritsar', 'Amritsar'), ('Jalandhar', 'Jalandhar'), ('Patiala', 'Patiala'), ('Bathinda', 'Bathinda'), ('Hoshiarpur', 'Hoshiarpur'), ('Batala', 'Batala'), ('Mohali', 'Mohali'), ('Abohar', 'Abohar'), ('Pathankot', 'Pathankot'), ('Moga', 'Moga'), ('Malerkotla', 'Malerkotla'), ('Khanna', 'Khanna'), ('Muktasar', 'Muktasar'), ('Barnala', 'Barnala'), ('Firozpur', 'Firozpur'), ('Kapurthala', 'Kapurthala'), ('Phagwara', 'Phagwara'), ('Zirakpur', 'Zirakpur'), ('Rajpura', 'Rajpura'))), ('Puducherry', (('Pondicherry', 'Pondicherry'), ('Ozhukarai', 'Ozhukarai'), ('Karaikal', 'Karaikal'))), ('Rajasthan', (('Jaipur', 'Jaipur'), ('Jodhpur', 'Jodhpur'), ('Kota', 'Kota'), ('Bikaner', 'Bikaner'), ('Ajmer', 'Ajmer'), ('Udaipur', 'Udaipur'), ('Bhilwara', 'Bhilwara'), ('Alwar', 'Alwar'), ('Bharatpur', 'Bharatpur'), ('Sri Ganganagar', 'Sri Ganganagar'), ('Sikar', 'Sikar'), ('Pali', 'Pali'), ('Barmer', 'Barmer'), ('Tonk', 'Tonk'), ('Kishangarh', 'Kishangarh'), ('Chittorgarh', 'Chittorgarh'), ('Beawar', 'Beawar'), ('Hanumangarh', 'Hanumangarh'), ('Dholpur', 'Dholpur'), ('Gangapur', 'Gangapur'), ('Sawai Madhopur', 'Sawai Madhopur'), ('Churu', 'Churu'), ('Baran', 'Baran'), ('Makrana', 'Makrana'), ('Nagaur', 'Nagaur'), ('Hindaun', 'Hindaun'), ('Bhiwadi', 'Bhiwadi'), ('Bundi', 'Bundi'), ('Sujangarh', 'Sujangarh'), ('Jhunjhunu', 'Jhunjhunu'), ('Banswara', 'Banswara'), ('Sardarshahar', 'Sardarshahar'), ('Fatehpur', 'Fatehpur'), ('Dausa', 'Dausa'), ('Karauli', 'Karauli'))), ('Sikkim', (('Gangtok', 'Gangtok'),)), ('Telangana', (('Hyderabad', 'Hyderabad'), ('Warangal', 'Warangal'), ('Nizamabad', 'Nizamabad'), ('Karimnagar', 'Karimnagar'), ('Ramagundam', 'Ramagundam'), ('Khammam', 'Khammam'), ('Mahbubnagar', 'Mahbubnagar'), ('Nalgonda', 'Nalgonda'), ('Adilabad', 'Adilabad'), ('Siddipet', 'Siddipet'), ('Suryapet', 'Suryapet'), ('Miryalaguda', 'Miryalaguda'), ('Jagtial', 'Jagtial'), ('Mancherial', 'Mancherial'), ('Kothagudem', 'Kothagudem'))), ('Tamil Nadu', (('Chennai', 'Chennai'), ('Coimbatore', 'Coimbatore'), ('Madurai', 'Madurai'), ('Tiruchirappalli', 'Tiruchirappalli'), ('Tirupur', 'Tirupur'), ('Salem', 'Salem'), ('Erode', 'Erode'), ('Tirunelveli', 'Tirunelveli'), ('Vellore', 'Vellore'), ('Tuticorin', 'Tuticorin'), ('Gudiyatham', 'Gudiyatham'), ('Nagercoil', 'Nagercoil'), ('Thanjavur', 'Thanjavur'), ('Dindigul', 'Dindigul'), ('Vaniyambadi', 'Vaniyambadi'), ('Cuddalore', 'Cuddalore'), ('Komarapalayam', 'Komarapalayam'), ('Kanchipuram', 'Kanchipuram'), ('Ambur', 'Ambur'), ('Tiruvannamalai', 'Tiruvannamalai'), ('Pudukkottai', 'Pudukkottai'), ('Kumbakonam', 'Kumbakonam'), ('Rajapalayam', 'Rajapalayam'), ('Hosur', 'Hosur'), ('Karaikudi', 'Karaikudi'), ('Neyveli', 'Neyveli'), ('Nagapattinam', 'Nagapattinam'), ('Viluppuram', 'Viluppuram'), ('Paramakudi', 'Paramakudi'), ('Tiruchengode', 'Tiruchengode'), ('Kovilpatti', 'Kovilpatti'), ('Theni-Allinagaram', 'Theni-Allinagaram'), ('Kadayanallur', 'Kadayanallur'), ('Pollachi', 'Pollachi'), ('Ooty', 'Ooty'))), ('Tripura', (('Agartala', 'Agartala'),)), ('Uttar Pradesh', (('Kanpur', 'Kanpur'), ('Lucknow', 'Lucknow'), ('Ghaziabad', 'Ghaziabad'), ('Agra', 'Agra'), ('Varanasi', 'Varanasi'), ('Meerut', 'Meerut'), ('Allahabad', 'Allahabad'), ('Bareilly', 'Bareilly'), ('Aligarh', 'Aligarh'), ('Moradabad', 'Moradabad'), ('Saharanpur', 'Saharanpur'), ('Gorakhpur', 'Gorakhpur'), ('Faizabad', 'Faizabad'), ('Firozabad', 'Firozabad'), ('Jhansi', 'Jhansi'), ('Muzaffarnagar', 'Muzaffarnagar'), ('Mathura', 'Mathura'), ('Budaun', 'Budaun'), ('Rampur', 'Rampur'), ('Shahjahanpur', 'Shahjahanpur'), ('Farrukhabad', 'Farrukhabad'), ('Mau', 'Mau'), ('Hapur', 'Hapur'), ('Noida', 'Noida'), ('Etawah', 'Etawah'), ('Mirzapur', 'Mirzapur'), ('Bulandshahr', 'Bulandshahr'), ('Sambhal', 'Sambhal'), ('Amroha', 'Amroha'), ('Hardoi', 'Hardoi'), ('Fatehpur', 'Fatehpur'), ('Raebareli', 'Raebareli'), ('Orai', 'Orai'), ('Sitapur', 'Sitapur'), ('Bahraich', 'Bahraich'), ('Modinagar', 'Modinagar'), ('Unnao', 'Unnao'), ('Jaunpur', 'Jaunpur'), ('Lakhimpur', 'Lakhimpur'), ('Hathras', 'Hathras'), ('Banda', 'Banda'), ('Pilibhit', 'Pilibhit'), ('Barabanki', 'Barabanki'), ('Mughalsarai', 'Mughalsarai'), ('Khurja', 'Khurja'), ('Gonda', 'Gonda'), ('Mainpuri', 'Mainpuri'), ('Lalitpur', 'Lalitpur'), ('Etah', 'Etah'), ('Deoria', 'Deoria'), ('Ujhani', 'Ujhani'), ('Ghazipur', 'Ghazipur'), ('Sultanpur', 'Sultanpur'), ('Azamgarh', 'Azamgarh'), ('Bijnor', 'Bijnor'), ('Sahaswan', 'Sahaswan'), ('Basti', 'Basti'), ('Chandausi', 'Chandausi'), ('Akbarpur', 'Akbarpur'), ('Ballia', 'Ballia'), ('Mubarakpur', 'Mubarakpur'), ('Tanda', 'Tanda'), ('Greater Noida', 'Greater Noida'), ('Shikohabad', 'Shikohabad'), ('Shamli', 'Shamli'), ('Baraut', 'Baraut'), ('Khair', 'Khair'), ('Kasganj', 'Kasganj'), ('Auraiya', 'Auraiya'), ('Khatauli', 'Khatauli'), ('Deoband', 'Deoband'), ('Nagina', 'Nagina'), ('Mahoba', 'Mahoba'), ('Muradnagar', 'Muradnagar'), ('Bhadohi', 'Bhadohi'), ('Dadri', 'Dadri'), ('Pratapgarh', 'Pratapgarh'), ('Najibabad', 'Najibabad'))), ('Uttarakhand', (('Dehradun', 'Dehradun'), ('Haridwar', 'Haridwar'), ('Roorkee', 'Roorkee'), ('Haldwani', 'Haldwani'), ('Rudrapur', 'Rudrapur'), ('Kashipur', 'Kashipur'), ('Rishikesh', 'Rishikesh'))), ('West Bengal', (('Kolkata', 'Kolkata'), ('Asansol', 'Asansol'), ('Siliguri', 'Siliguri'), ('Durgapur', 'Durgapur'), ('Bardhaman', 'Bardhaman'), ('Malda', 'Malda'), ('Baharampur', 'Baharampur'), ('Habra', 'Habra'), ('Jalpaiguri', 'Jalpaiguri'), ('Kharagpur', 'Kharagpur'), ('Shantipur', 'Shantipur'), ('Dankuni', 'Dankuni'), ('Dhulian', 'Dhulian'), ('Ranaghat', 'Ranaghat'), ('Haldia', 'Haldia'), ('Raiganj', 'Raiganj'), ('Krishnanagar', 'Krishnanagar'), ('Nabadwip', 'Nabadwip'), ('Midnapore', 'Midnapore'), ('Balurghat', 'Balurghat'), ('Basirhat', 'Basirhat'), ('Bankura', 'Bankura'), ('Chakdaha', 'Chakdaha'), ('Darjeeling', 'Darjeeling'), ('Alipurduar', 'Alipurduar'), ('Purulia', 'Purulia'), ('Jangipur', 'Jangipur'), ('Bangaon', 'Bangaon'), ('Cooch Behar', 'Cooch Behar'), ('Bolpur', 'Bolpur'), ('Kanthi', 'Kanthi')))], max_length=20, null=True)),
                ('zip_code', models.IntegerField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('profile_data_id', models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='addresses', to='SportingBuddiesApp.profiles')),
            ],
        ),
    ]
