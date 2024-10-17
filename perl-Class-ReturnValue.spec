%define upstream_name    Class-ReturnValue
%define upstream_version 0.55

Name:		perl-%{upstream_name}
Version:	%perl_convert_version %{upstream_version}
Release:	5

Summary:	Class-ReturnValue module for perl 
License:	GPL+ or Artistic
Group:		Development/Perl
Url:		https://search.cpan.org/dist/%{upstream_name}
Source0:	http://www.cpan.org/modules/by-module/Class/%{upstream_name}-%{upstream_version}.tar.bz2

BuildRequires:	perl-devel
BuildRequires:	perl(Devel::StackTrace)
BuildArch:	noarch

%description
This module provides a return-value object that lets you treat it as as a
boolean, array or object.

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

%build
perl Makefile.PL INSTALLDIRS=vendor
%make

%check
make test

%install
%makeinstall_std

%files
%doc Changes
%{perl_vendorlib}/Class/ReturnValue.pm
%{_mandir}/*/*


%changelog
* Sat May 28 2011 Funda Wang <fwang@mandriva.org> 0.550.0-2mdv2011.0
+ Revision: 680826
- mass rebuild

* Sat Aug 01 2009 Jérôme Quelin <jquelin@mandriva.org> 0.550.0-1mdv2011.0
+ Revision: 406876
- rebuild using %%perl_convert_version

* Wed Jul 30 2008 Thierry Vignaud <tv@mandriva.org> 0.55-3mdv2009.0
+ Revision: 256029
- rebuild

* Fri Dec 21 2007 Olivier Blin <oblin@mandriva.com> 0.55-1mdv2008.1
+ Revision: 136684
- restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request

* Wed Aug 22 2007 Guillaume Rousse <guillomovitch@mandriva.org> 0.55-1mdv2008.0
+ Revision: 69215
- update to new version 0.55

* Wed Aug 15 2007 Guillaume Rousse <guillomovitch@mandriva.org> 0.54-1mdv2008.0
+ Revision: 63925
- update to new version 0.54


* Mon Aug 28 2006 Olivier Thauvin <nanardon@mandriva.org>
+ 2006-08-28 14:45:25 (58405)
- mkrel
- check section

* Mon Aug 28 2006 Olivier Thauvin <nanardon@mandriva.org>
+ 2006-08-28 14:40:52 (58404)
Import perl-Class-ReturnValue

* Wed Jul 20 2005 Rafael Garcia-Suarez <rgarciasuarez@mandriva.com> 0.53-1mdk
- 0.53

* Wed Jul 13 2005 Oden Eriksson <oeriksson@mandriva.com> 0.52-1mdk
- initial Mandriva package

