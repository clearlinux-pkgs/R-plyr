#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : R-plyr
Version  : 1.8.3
Release  : 19
URL      : http://cran.r-project.org/src/contrib/plyr_1.8.3.tar.gz
Source0  : http://cran.r-project.org/src/contrib/plyr_1.8.3.tar.gz
Summary  : Tools for Splitting, Applying and Combining Data
Group    : Development/Tools
License  : MIT
Requires: R-plyr-lib
Requires: R-Rcpp
Requires: R-testthat
BuildRequires : R-Rcpp
BuildRequires : R-testthat
BuildRequires : clr-R-helpers

%description
[![Build Status](https://travis-ci.org/hadley/plyr.png?branch=master)](https://travis-ci.org/hadley/plyr) [![Coverage Status](https://coveralls.io/repos/hadley/plyr/badge.svg?branch=master)](https://coveralls.io/r/hadley/plyr?branch=master)

%package lib
Summary: lib components for the R-plyr package.
Group: Libraries

%description lib
lib components for the R-plyr package.


%prep
%setup -q -c -n plyr

%build

%install
rm -rf %{buildroot}
export LANG=C
export CFLAGS="$CFLAGS -O3 -flto -ffunction-sections -fno-semantic-interposition "
export CXXFLAGS="$CXXFLAGS -O3 -flto -ffunction-sections -fno-semantic-interposition "
export AR=gcc-ar
export RANLIB=gcc-ranlib
export LDFLAGS="$LDFLAGS  -Wl,-z -Wl,relro"
mkdir -p %{buildroot}/usr/lib64/R/library
R CMD INSTALL --install-tests --build  -l %{buildroot}/usr/lib64/R/library plyr
%{__rm} -rf %{buildroot}%{_datadir}/R/library/R.css
%check
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=intel.com,localhost
export _R_CHECK_FORCE_SUGGESTS_=false
R CMD check --no-manual --no-examples --no-codoc -l %{buildroot}/usr/lib64/R/library plyr || :


%files
%defattr(-,root,root,-)
/usr/lib64/R/library/plyr/CITATION
/usr/lib64/R/library/plyr/DESCRIPTION
/usr/lib64/R/library/plyr/INDEX
/usr/lib64/R/library/plyr/LICENSE
/usr/lib64/R/library/plyr/Meta/Rd.rds
/usr/lib64/R/library/plyr/Meta/data.rds
/usr/lib64/R/library/plyr/Meta/hsearch.rds
/usr/lib64/R/library/plyr/Meta/links.rds
/usr/lib64/R/library/plyr/Meta/nsInfo.rds
/usr/lib64/R/library/plyr/Meta/package.rds
/usr/lib64/R/library/plyr/NAMESPACE
/usr/lib64/R/library/plyr/R/plyr
/usr/lib64/R/library/plyr/R/plyr.rdb
/usr/lib64/R/library/plyr/R/plyr.rdx
/usr/lib64/R/library/plyr/data/Rdata.rdb
/usr/lib64/R/library/plyr/data/Rdata.rds
/usr/lib64/R/library/plyr/data/Rdata.rdx
/usr/lib64/R/library/plyr/help/AnIndex
/usr/lib64/R/library/plyr/help/aliases.rds
/usr/lib64/R/library/plyr/help/paths.rds
/usr/lib64/R/library/plyr/help/plyr.rdb
/usr/lib64/R/library/plyr/help/plyr.rdx
/usr/lib64/R/library/plyr/html/00Index.html
/usr/lib64/R/library/plyr/html/R.css
/usr/lib64/R/library/plyr/libs/symbols.rds

%files lib
%defattr(-,root,root,-)
/usr/lib64/R/library/plyr/libs/plyr.so
