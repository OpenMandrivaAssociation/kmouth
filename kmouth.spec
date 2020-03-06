%define stable %([ "`echo %{version} |cut -d. -f3`" -ge 70 ] && echo -n un; echo -n stable)

Name:		kmouth
Version:	19.12.3
Release:	1
Epoch:		2
Summary:	A type-and-say front end for speech synthesizers
Group:		Graphical desktop/KDE
License:	GPLv2 and GFDL
URL:		http://www.kde.org/applications/utilities/kmouth/
Source0:	http://download.kde.org/%{stable}/release-service/%{version}/src/%{name}-%{version}.tar.xz
BuildRequires:	cmake cmake(ECM) ninja
BuildRequires:	cmake(KF5Completion) cmake(KF5Config) cmake(KF5ConfigWidgets) cmake(KF5CoreAddons) cmake(KF5I18n)
BuildRequires:	cmake(KF5KIO) cmake(KF5WidgetsAddons) cmake(KF5XmlGui)
BuildRequires:	cmake(Qt5Core) cmake(Qt5Gui) cmake(Qt5PrintSupport) cmake(Qt5TextToSpeech) cmake(Qt5Widgets) cmake(Qt5Xml)
BuildRequires:	cmake(KF5DocTools)
BuildRequires:	cmake(KF5Crash)

%description
KMouth is a program which enables persons that cannot speak to let their
computer speak, e.g. mutal people or people who have lost their voice. It has a
text input field and speaks the sentences that you enter. It also has support
for user defined phrasebooks.

%files -f %{name}.lang
%doc AUTHORS COPYING COPYING.DOC
%{_sysconfdir}/xdg/kmouthrc
%{_bindir}/kmouth
%{_datadir}/applications/org.kde.kmouth.desktop
%{_datadir}/kmouth
%{_datadir}/kxmlgui5/kmouth
%{_datadir}/icons/*/*/*/*
%{_datadir}/metainfo/org.kde.kmouth.appdata.xml
%{_mandir}/man1/kmouth.1*

%prep
%setup -q

%build
%cmake_kde5
%ninja

%install
%ninja_install -C build
%find_lang %{name} --all-name --with-html --with-man
