%define module Catalyst-Plugin-HTML-Widget
%define name	perl-%{module}
%define	modprefix Catalyst
%define version 1.1
%define release %mkrel 6

Summary:	HTML Widget And Validation Framework
Name:		%{name}
Version:	%{version}
Release:	%{release}
License:	Artistic/GPL
Group:		Development/Perl
URL:		http://search.cpan.org/dist/%{module}/
Source:     http://www.cpan.org/modules/by-module/Date/%{module}-%{version}.tar.bz2
BuildRequires:	perl(Catalyst) >= 5.5
BuildRequires:	perl(HTML::Widget)
BuildArch:	noarch
Buildroot:	%{_tmppath}/%{version}-%{release}

%description
HTML Widget And Validation Framework

%prep
%setup -q -n %{module}-%{version}

%build
%__perl Makefile.PL INSTALLDIRS=vendor --skipdeps
%make

%check
%__make test

%install
rm -rf %{buildroot}
%makeinstall_std

%files
%defattr(-,root,root)
%doc Changes README
%{_mandir}/*/*
%{perl_vendorlib}/%{modprefix}

%clean
rm -rf %{buildroot}
