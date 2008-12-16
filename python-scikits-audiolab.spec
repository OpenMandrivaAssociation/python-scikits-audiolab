%define tarname	scikits.audiolab
%define name	python-scikits-audiolab
%define version	0.10.1
%define release	%mkrel 1

Summary:	Python audio file I/O using numpy arrays
Name:		%{name}
Version:	%{version}
Release:	%{release}
Source0:	http://pypi.python.org/packages/source/s/%{tarname}/%{tarname}-%{version}.tar.gz
License:	LGPLv2.1
Group: 		Development/Python
Url:		http://www.ar.media.kyoto-u.ac.jp/members/david/softwares/audiolab
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot
Requires:	libsndfile1, libalsa
Requires:	python-numpy >= 1.0
BuildRequires:	sndfile-devel, libalsa-devel
BuildRequires:	python-numpy >= 1.0 
%py_requires -d

%description
Audiolab is a Python package for audio file I/O using numpy arrays. It
supports many different audio formats, including wav, aiff, au, flac,
ogg, and htk. It can also be used to output sound to an audio device
via ALSA.

%prep
%setup -q -n %{tarname}-%{version}

%build
%__python setup.py build

%install
%__rm -rf %{buildroot}
%__python setup.py install --root=%{buildroot}

%clean
%__rm -rf %{buildroot}

%files
%defattr(-,root,root)
%doc docs/pdf/*.pdf README.txt Changelog COPYING.txt NEWS
%py_sitedir/scikits*
