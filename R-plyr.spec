#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : R-plyr
Version  : 1.8.7
Release  : 88
URL      : https://cran.r-project.org/src/contrib/plyr_1.8.7.tar.gz
Source0  : https://cran.r-project.org/src/contrib/plyr_1.8.7.tar.gz
Summary  : Tools for Splitting, Applying and Combining Data
Group    : Development/Tools
License  : MIT
Requires: R-plyr-lib = %{version}-%{release}
Requires: R-Rcpp
BuildRequires : R-Rcpp
BuildRequires : buildreq-R

%description
to break a big problem down into manageable pieces, operate on each
    piece and then put all the pieces back together.  For example, you
    might want to fit a model to each spatial location or time point in
    your study, summarise data by panels or collapse high-dimensional
    arrays to simpler summary statistics. The development of 'plyr' has
    been generously supported by 'Becton Dickinson'.

%package lib
Summary: lib components for the R-plyr package.
Group: Libraries

%description lib
lib components for the R-plyr package.


%prep
%setup -q -c -n plyr
cd %{_builddir}/plyr

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1648233499

%install
export SOURCE_DATE_EPOCH=1648233499
rm -rf %{buildroot}
export LANG=C.UTF-8
export CFLAGS="$CFLAGS -O3 -flto -fno-semantic-interposition "
export FCFLAGS="$FFLAGS -O3 -flto -fno-semantic-interposition "
export FFLAGS="$FFLAGS -O3 -flto -fno-semantic-interposition "
export CXXFLAGS="$CXXFLAGS -O3 -flto -fno-semantic-interposition "
export AR=gcc-ar
export RANLIB=gcc-ranlib
export LDFLAGS="$LDFLAGS  -Wl,-z -Wl,relro"
mkdir -p %{buildroot}/usr/lib64/R/library

mkdir -p ~/.R
mkdir -p ~/.stash
echo "CFLAGS = $CFLAGS -march=x86-64-v3 -ftree-vectorize -mno-vzeroupper" > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=x86-64-v3 -ftree-vectorize -mno-vzeroupper " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=x86-64-v3 -ftree-vectorize -mno-vzeroupper " >> ~/.R/Makevars
R CMD INSTALL --install-tests --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library plyr
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx2 ; mv $i.avx2 ~/.stash/; done
echo "CFLAGS = $CFLAGS -march=x86-64-v4 -ftree-vectorize  -mno-vzeroupper " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=x86-64-v4 -ftree-vectorize  -mno-vzeroupper " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=x86-64-v4 -ftree-vectorize -mno-vzeroupper  " >> ~/.R/Makevars
R CMD INSTALL --preclean --install-tests --no-test-load --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library plyr
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx512 ; mv $i.avx512 ~/.stash/; done
echo "CFLAGS = $CFLAGS -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --preclean --install-tests --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library plyr
cp ~/.stash/* %{buildroot}/usr/lib64/R/library/*/libs/ || :
%{__rm} -rf %{buildroot}%{_datadir}/R/library/R.css
%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export _R_CHECK_FORCE_SUGGESTS_=false
R CMD check --no-manual --no-examples --no-codoc plyr || :


%files
%defattr(-,root,root,-)
/usr/lib64/R/library/plyr/CITATION
/usr/lib64/R/library/plyr/DESCRIPTION
/usr/lib64/R/library/plyr/INDEX
/usr/lib64/R/library/plyr/LICENSE
/usr/lib64/R/library/plyr/Meta/Rd.rds
/usr/lib64/R/library/plyr/Meta/data.rds
/usr/lib64/R/library/plyr/Meta/features.rds
/usr/lib64/R/library/plyr/Meta/hsearch.rds
/usr/lib64/R/library/plyr/Meta/links.rds
/usr/lib64/R/library/plyr/Meta/nsInfo.rds
/usr/lib64/R/library/plyr/Meta/package.rds
/usr/lib64/R/library/plyr/NAMESPACE
/usr/lib64/R/library/plyr/NEWS.md
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
/usr/lib64/R/library/plyr/tests/testthat.R
/usr/lib64/R/library/plyr/tests/testthat/quickdf.r
/usr/lib64/R/library/plyr/tests/testthat/test-arrange.r
/usr/lib64/R/library/plyr/tests/testthat/test-array.r
/usr/lib64/R/library/plyr/tests/testthat/test-count.r
/usr/lib64/R/library/plyr/tests/testthat/test-data-frame.r
/usr/lib64/R/library/plyr/tests/testthat/test-debug.r
/usr/lib64/R/library/plyr/tests/testthat/test-empty.r
/usr/lib64/R/library/plyr/tests/testthat/test-id.r
/usr/lib64/R/library/plyr/tests/testthat/test-idf.r
/usr/lib64/R/library/plyr/tests/testthat/test-inform.r
/usr/lib64/R/library/plyr/tests/testthat/test-join.r
/usr/lib64/R/library/plyr/tests/testthat/test-list.r
/usr/lib64/R/library/plyr/tests/testthat/test-manip.r
/usr/lib64/R/library/plyr/tests/testthat/test-mapply.r
/usr/lib64/R/library/plyr/tests/testthat/test-mutate.r
/usr/lib64/R/library/plyr/tests/testthat/test-ninteraction.r
/usr/lib64/R/library/plyr/tests/testthat/test-parallel.r
/usr/lib64/R/library/plyr/tests/testthat/test-progress.r
/usr/lib64/R/library/plyr/tests/testthat/test-quote.r
/usr/lib64/R/library/plyr/tests/testthat/test-rbind.matrix.r
/usr/lib64/R/library/plyr/tests/testthat/test-rbind.r
/usr/lib64/R/library/plyr/tests/testthat/test-rename.r
/usr/lib64/R/library/plyr/tests/testthat/test-replicate.r
/usr/lib64/R/library/plyr/tests/testthat/test-revalue.r
/usr/lib64/R/library/plyr/tests/testthat/test-rply.r
/usr/lib64/R/library/plyr/tests/testthat/test-simplify-df.r
/usr/lib64/R/library/plyr/tests/testthat/test-split-data-frame.r
/usr/lib64/R/library/plyr/tests/testthat/test-split-indices.r
/usr/lib64/R/library/plyr/tests/testthat/test-split-labels.r
/usr/lib64/R/library/plyr/tests/testthat/test-summarise.r
/usr/lib64/R/library/plyr/tests/testthat/test-utils.r

%files lib
%defattr(-,root,root,-)
/usr/lib64/R/library/plyr/libs/plyr.so
/usr/lib64/R/library/plyr/libs/plyr.so.avx2
/usr/lib64/R/library/plyr/libs/plyr.so.avx512
