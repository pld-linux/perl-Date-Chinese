#
# Conditional build:
%bcond_without	tests	# do perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define	pdir	Date
%define pnam	Chinese
Summary:	Date::Chinese - calculate dates in the Chinese calendar
Summary(pl):	Date::Chinese - obliczanie dat w kalendarzu chiñskim
Name:		perl-Date-Chinese
Version:	1.03
Release:	1
# same as perl
License:	GPL or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	eacb27452890572fadf9d5b6b137d3ff
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Perlish interface to Chinese Calendar.

%description -l pl
Perlowy interfejs do kalendarza chiñskiego.

%prep
%setup -q -n %{pdir}-%{pnam}-1.3

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
