changename.py ���޸��ļ��������ֵ�,�����Ų����������
getAlTitle.py �ǻ�ȡtitle��
Titletookit �ǲ���ķ����
polang ��chrome����İ�װ�ļ�


1.0 ֻ����Ҫ��ȡtitle֮�����ʹ��,���Ҳ�������title������,ÿ�β���ֻ��ȡtitle.txt����ļ�,���ᰴ�ղ�ͬ������ȥ��ȡ��������Դ.
����ÿ�����궼��Ҫ�ֶ��޸�titile.txt����ļ�

�÷�
1;���Ȱ�װ virtualenv  https://virtualenv.pypa.io/en/stable/userguide/
2:�½�һ���ļ��� TitleTooltik,����TitleTooltik
3:���� ����ռ� virtualenv env
4:����virtualenv source env/bin/activate
5:��װ��Ҫ�İ�  pip install -r requirements.txt 
6:��װnltk  http://www.nltk.org/install.html
Install NLTK: run sudo pip install -U nltk  (�Ұ�װ�����βųɹ�,Ҳʹ����pip install nltk ��仰��װ)
Install Numpy (optional): run sudo pip install -U numpy
Test installation: run python then type import nltk
��������ǳɹ���
7:����nltk data
import nltk
>>> nltk.download()
����run python -m nltk.downloader all ��װ
centos ��data��/usr/share/nltk_data  ����

8:�ϴ�titletookit�����ļ���������
9:����  gunicorn -w 4 -b 0.0.0.0:5586 run:app ����������  

ע��: 0.0.0.0:5586 ��Ҫ��0.0.0.0 �������� 127.0.0.1 ,��Ȼ�������ܷ���