"""Verify the actual distributed APK and active download metadata using public tools."""
from pathlib import Path
import collections,hashlib,json,os,re,subprocess,sys,zipfile
apk=Path('downloads/ExamReadySA-v1.2.4.apk')
report=json.loads(Path('downloads/ExamReadySA-v1.2.4-verification.json').read_text())
expected_signer='dd4c342fcfa66ac2d9b7b37c1a4cd55d4c998be78dbe2479489b031d6fe38dc2'
assert apk.stat().st_size==report['sizeBytes']
assert hashlib.sha256(apk.read_bytes()).hexdigest()==report['sha256']
assert report['sourceCommit']==sys.argv[1]
assert report['versionCode']==12 and report['versionName']=='1.2.4'
assert report['packageName']=='za.co.examready.prototype'
assert report['signingCertificateSha256']==expected_signer
assert report['progressPreserved'] is True and report['signedOfflineSmoke'] is True
assert report['upgradeFrom']==['1.2.2','1.2.3']
tools=Path(os.environ['ANDROID_HOME'])/'build-tools/34.0.0'
sig=subprocess.check_output([str(tools/'apksigner'),'verify','--verbose','--print-certs',str(apk)],text=True)
assert 'Signer #1 certificate SHA-256 digest: '+expected_signer in sig
assert 'Verified using v2 scheme (APK Signature Scheme v2): true' in sig
badging=subprocess.check_output([str(tools/'aapt'),'dump','badging',str(apk)],text=True)
assert "package: name='za.co.examready.prototype' versionCode='12' versionName='1.2.4'" in badging
assert 'application-debuggable' not in badging
assert 'com.google.android.gms.permission.AD_ID' not in badging
bank=json.loads(zipfile.ZipFile(apk).read('assets/questions.json'))
assert len(bank)==9340 and len({q['id'] for q in bank})==9340
counts=collections.Counter((q['grade'],q['subject']) for q in bank)
assert len(counts)==33
for grade in (10,11,12):
 for subject in ('Accounting','Business Studies','Economics'):
  assert counts[grade,subject]==500
  assert {q['difficulty'] for q in bank if q['grade']==grade and q['subject']==subject}=={'Easy','Medium','Hard'}
by_id={q['id']:q for q in bank}
for version in ('1.2.2','1.2.3'):
 old=json.loads(zipfile.ZipFile('downloads/ExamReadySA-v'+version+'.apk').read('assets/questions.json'))
 assert len(old)==4840
 for q in old:
  assert q['id'] in by_id
  assert all(q.get(k)==by_id[q['id']].get(k) for k in ('grade','subject','question','options','answer')),q['id']
latest=json.loads(Path('updates/latest.json').read_text())
policy=json.loads(Path('updates/android.json').read_text())
assert latest['packageName']==policy['packageName']=='za.co.examready.prototype'
assert policy['minimumSupportedVersionCode']==1
assert policy['latestVersionCode']==latest['versionCode']
assert policy['latestVersionName']==latest['versionName']

if latest['versionCode'] == 12:
 for key in ('versionCode','versionName','sha256','sizeBytes','apkPath'):assert latest[key]==report[key],key
elif latest['versionCode'] in (13,14):
 current_report_path = Path('downloads/ExamReadySA-v1.2.6-verification.json') if latest['versionCode']==14 else Path('downloads/release-verification.json')
 current_report=json.loads(current_report_path.read_text())
 apk_current=Path(latest['apkPath'])
 assert apk_current.is_file()
 assert current_report['packageName']==latest['packageName']=='za.co.examready.prototype'
 assert current_report['versionCode']==latest['versionCode']
 assert current_report['versionName']==latest['versionName']
 assert current_report['apkPath']==latest['apkPath']
 assert current_report['sizeBytes']==latest['sizeBytes']==apk_current.stat().st_size
 assert current_report['sha256']==latest['sha256']==hashlib.sha256(apk_current.read_bytes()).hexdigest()
 assert current_report['signingCertificateSha256']==expected_signer
 assert current_report['progressPreserved'] is True and current_report['signedOfflineSmoke'] is True
 if latest['versionCode']==14:
  assert current_report['sourceCommit']=='481c52dcc3b9ab6523f4a0cabadc148bcfb8ae48'
  assert current_report['upgradeFrom']==['1.2.2','1.2.3','1.2.4','1.2.5']
 sig=subprocess.check_output([str(tools/'apksigner'),'verify','--verbose','--print-certs',str(apk_current)],text=True)
 assert 'Signer #1 certificate SHA-256 digest: '+expected_signer in sig
 assert 'Verified using v2 scheme (APK Signature Scheme v2): true' in sig
 badging_current=subprocess.check_output([str(tools/'aapt'),'dump','badging',str(apk_current)],text=True)
 expected_name=current_report['versionName']
 expected_code=str(current_report['versionCode'])
 assert f"package: name='za.co.examready.prototype' versionCode='{expected_code}' versionName='{expected_name}'" in badging_current
 assert 'application-debuggable' not in badging_current
 bank_current=json.loads(zipfile.ZipFile(apk_current).read('assets/questions.json'))
 assert len(bank_current)==latest['questionCount']==9340
 assert len({q['id'] for q in bank_current})==9340
else:
 # A legacy v1.2.3 metadata state is retained only while preparing v1.2.4.
 assert latest['versionCode']==policy['latestVersionCode']==11
print('PUBLIC_RELEASE_VERIFY_PASS: historical signed APK, current APK checksum/signature/version, practice bank, preserved question IDs and optional update policy verified.')
