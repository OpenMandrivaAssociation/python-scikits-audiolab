%define tarname	scikits.audiolab
%define name	python-scikits-audiolab
%define version	0.11.0
%define release	%mkrel 2

Summary:	Python audio file I/O using numpy arrays
Name:		%{name}
Version:	%{version}
Release:	%{release}
Source0:	http://pypi.python.org/packages/source/s/%{tarname}/%{tarname}-%{version}.tar.gz
Source1:	site.cfg
Patch0:		matapi.patch
License:	LGPLv2.1
Group: 		Development/Python
Url:		http://www.ar.media.kyoto-u.ac.jp/members/david/softwares/audiolab
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot
Requires:	python-numpy >= 1.0
BuildRequires:	sndfile-devel, libalsa-devel
BuildRequires:	python-numpy-devel >= 1.0, python-setuptools
%py_requires -d

%description
Audiolab is a Python package for audio file I/O using numpy arrays. It
supports many different audio formats, including wav, aiff, au, flac,
ogg, and htk. It can also be used to output sound to an audio device
via ALSA.

%prep
%setup -q -n %{tarname}-%{version}
%__cp %SOURCE1 .
%patch0 -p0

%build
%__python setup.py build
find . -name .buildinfo | xargs rm -rf

%install
%__rm -rf %{buildroot}
%__python setup.py install --root=%{buildroot}

%clean
%__rm -rf %{buildroot}

%files
%defattr(-,root,root)
%doc docs/html README.txt Changelog COPYING.txt NEWS
%py_platsitedir/scikits*


%changelog
* Fri Oct 29 2010 Michael Scherer <misc@mandriva.org> 0.11.0-2mdv2011.0
+ Revision: 590088
- rebuild for python 2.7

* Sun Jul 25 2010 Lev Givon <lev@mandriva.org> 0.11.0-1mdv2011.0
+ Revision: 558953
- Update to 0.11.0.

* Fri Aug 28 2009 Lev Givon <lev@mandriva.org> 0.10.2-2mdv2010.0
+ Revision: 421946
- Patch bug in matapi.py.

* Thu Apr 02 2009 Lev Givon <lev@mandriva.org> 0.10.2-1mdv2010.0
+ Revision: 363429
- Update to 0.10.2.

* Fri Dec 26 2008 Funda Wang <fwang@mandriva.org> 0.10.1-2mdv2009.1
+ Revision: 319422
- rebuild for new python

* Tue Dec 16 2008 Lev Givon <lev@mandriva.org> 0.10.1-1mdv2009.1
+ Revision: 315000
- import python-scikits-audiolab


