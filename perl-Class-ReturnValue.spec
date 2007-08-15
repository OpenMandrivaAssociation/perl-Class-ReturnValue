%define real_name Class-ReturnValue

Summary:	Class-ReturnValue module for perl 
Name:		perl-%{real_name}
Version:	0.54
Release:	%mkrel 1
License:	GPL or Artistic
Group:		Development/Perl
URL:		http://search.cpan.org/dist/%{real_name}
Source0:	%{real_name}-%{version}.tar.bz2
BuildRequires:	perl-devel, perl-Devel-StackTrace
BuildArch:	noarch
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot

%description
This module provides a return-value object that lets you treat it as as a
boolean, array or object.

%prep
%setup -q -n %{real_name}-%{version} 

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor
%make

%check
make test

%install
rm -rf %{buildroot}
%makeinstall_std

%clean 
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%doc Changes
%{perl_vendorlib}/Class/ReturnValue.pm
%{_mandir}/*/*

