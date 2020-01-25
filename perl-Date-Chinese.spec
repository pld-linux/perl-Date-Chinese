#
# Conditional build:
%bcond_without	tests	# do perform "make test"

%define		pdir	Date
%define		pnam	Chinese
Summary:	Date::Chinese - calculate dates in the Chinese calendar
Summary(pl.UTF-8):	Date::Chinese - obliczanie dat w kalendarzu chińskim
Name:		perl-Date-Chinese
Version:	1.12
Release:	1
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	aba4a151ecf84acd9091ee8f56a1d50f
URL:		http://search.cpan.org/dist/Date-Chinese/
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Date::Chinese is Perlish interface to the Chinese Calendar.

%description -l pl.UTF-8
Date::Chinese stanowi interfejs perlowy do kalendarza chińskiego.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor

%{__make}

%{?with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%{perl_vendorlib}/Date/Chinese.pm
%{_mandir}/man3/*
