%define upstream_name    Catalyst-Plugin-HTML-Widget
%define upstream_version 1.1

Name:		perl-%{upstream_name}
Version:	%perl_convert_version %{upstream_version}
Release:	5

Summary:	HTML Widget And Validation Framework
License:	Artistic/GPL
Group:		Development/Perl
Url:		http://search.cpan.org/dist/%{upstream_name}/
Source0:	http://www.cpan.org/modules/by-module/Date/%{upstream_name}-%{upstream_version}.tar.bz2

BuildRequires:	perl-devel
BuildRequires:	perl(Catalyst) >= 5.500.0
BuildRequires:	perl(HTML::Widget)

BuildArch:	noarch

%description
HTML Widget And Validation Framework.

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

%build
perl Makefile.PL INSTALLDIRS=vendor --skipdeps
%make

%check
%make test

%install
%makeinstall_std

%files
%doc Changes README
%{_mandir}/*/*
%{perl_vendorlib}/Catalyst


%changelog
* Sat May 28 2011 Funda Wang <fwang@mandriva.org> 1.100.0-2mdv2011.0
+ Revision: 680735
- mass rebuild

* Sat Feb 13 2010 Jérôme Quelin <jquelin@mandriva.org> 1.100.0-1mdv2011.0
+ Revision: 505420
- rebuild using %%perl_convert_version

* Fri Sep 04 2009 Thierry Vignaud <tv@mandriva.org> 1.1-7mdv2010.0
+ Revision: 430271
- rebuild

* Wed Jul 30 2008 Thierry Vignaud <tv@mandriva.org> 1.1-6mdv2009.0
+ Revision: 255556
- rebuild

* Thu Dec 27 2007 Guillaume Rousse <guillomovitch@mandriva.org> 1.1-4mdv2008.1
+ Revision: 138595
- rebuild
- rebuild

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request


* Sun Aug 06 2006 Scott Karns <scottk@mandriva.org>
+ 2006-08-06 19:06:42 (53577)
- Spec file cleanup

* Sun Aug 06 2006 Scott Karns <scottk@mandriva.org>
+ 2006-08-06 18:54:02 (53544)
- import perl-Catalyst-Plugin-HTML-Widget-1.1-1mdk

* Tue Jan 18 2005 Scott Karns <scott@karnstech.com> 1.1-1mdk
- Initial Mdv RPM

