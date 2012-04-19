Name: kmouth
Summary: KMouth - Speech Synthesizer Frontend
Version: 4.8.2
Release: 1
Epoch: 2
Group: Graphical desktop/KDE
License: LGPLv2
URL: http://utils.kde.org/projects/kmouth
Source: ftp://ftp.kde.org/pub/kde/stable/%version/src/%{name}-%version.tar.xz
BuildRequires: kdelibs4-devel >= 2:%{version}

Obsoletes: kde4-kmouth < 4.0.68
Provides: kde4-kmouth = %version

%description
KMouth is a program which enables persons that cannot speak to let their 
computer speak, e.g. mutal people or people who have lost their voice. 
It has a text input field and speaks the sentences that you enter. It 
also has support for user defined phrasebooks.

%files 
%_kde_bindir/kmouth
%_kde_iconsdir/*/*/apps/kmouth.*
%_kde_datadir/apps/kmouth/icons/*/*/actions/*.png
%_kde_datadir/applications/kde4/kmouth.desktop
%_kde_datadir/apps/kmouth/*.rc
%_kde_datadir/config/kmouthrc
%_kde_datadir/apps/kmouth/books/*
%_kde_docdir/HTML/*/kmouth
%_mandir/man1/*

%prep
%setup -q

%build
%cmake_kde4

%make

%install
%makeinstall_std -C build

