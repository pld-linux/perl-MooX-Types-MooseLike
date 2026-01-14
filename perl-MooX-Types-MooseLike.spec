#
# Conditional build:
%bcond_without	tests		# do not perform "make test"
#
%define		pdir	MooX
%define		pnam	Types-MooseLike
Summary:	MooX::Types::MooseLike - some Moosish types and a type builder
Name:		perl-MooX-Types-MooseLike
Version:	0.28
Release:	3
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/MooX/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	ba30a142740694c3a01457c452dc5fa6
URL:		http://search.cpan.org/dist/MooX-Types-MooseLike/
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
%if %{with tests}
BuildRequires:	perl-Module-Runtime >= 0.014
BuildRequires:	perl-Moo >= 1.004002
BuildRequires:	perl-Test-Fatal >= 0.003
%endif
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This module provides a possibility to build your own set of Moose-like
types. These custom types can then be used to describe fields in
Moo-based classes.

See MooX::Types::MooseLike::Base for a list of available base types.
Its source also provides an example of how to build base types, along
with both parameterizable and non-parameterizable.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make}

%{?with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} pure_install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes README
%dir %{perl_vendorlib}/MooX/Types
%{perl_vendorlib}/MooX/Types/*.pm
%{perl_vendorlib}/MooX/Types/MooseLike
%{_mandir}/man3/*
