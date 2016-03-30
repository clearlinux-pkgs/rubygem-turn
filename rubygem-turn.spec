#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : rubygem-turn
Version  : 0.9.7
Release  : 4
URL      : https://rubygems.org/downloads/turn-0.9.7.gem
Source0  : https://rubygems.org/downloads/turn-0.9.7.gem
Summary  : No detailed summary available
Group    : Development/Tools
License  : MIT
Requires: rubygem-turn-bin
BuildRequires : ruby
BuildRequires : rubygem-ansi
BuildRequires : rubygem-indexer
BuildRequires : rubygem-mast
BuildRequires : rubygem-rake
BuildRequires : rubygem-rdoc

%description
# TURN - MiniTest Reporters [![Build status](https://api.travis-ci.org/turn-project/turn.png)](https://travis-ci.org/turn-project/turn)
by Tim Pease
http://rubygems.org/gems/turn

%package bin
Summary: bin components for the rubygem-turn package.
Group: Binaries

%description bin
bin components for the rubygem-turn package.


%prep
gem unpack %{SOURCE0}
%setup -q -D -T -n turn-0.9.7
gem spec %{SOURCE0} -l --ruby > rubygem-turn.gemspec

%build
gem build rubygem-turn.gemspec

%install
%global gem_dir $(ruby -e'puts Gem.default_dir')
gem install -V \
--local \
--force \
--install-dir .%{gem_dir} \
--bindir .%{_bindir} \
turn-0.9.7.gem

mkdir -p %{buildroot}%{gem_dir}
cp -pa .%{gem_dir}/* \
%{buildroot}%{gem_dir}

if [ -d .%{_bindir} ]; then
mkdir -p %{buildroot}%{_bindir}
cp -pa .%{_bindir}/* \
%{buildroot}%{_bindir}/
fi


%files
%defattr(-,root,root,-)
/usr/lib64/ruby/gems/2.3.0/cache/turn-0.9.7.gem
/usr/lib64/ruby/gems/2.3.0/gems/turn-0.9.7/CONTRIBUTING.md
/usr/lib64/ruby/gems/2.3.0/gems/turn-0.9.7/History.txt
/usr/lib64/ruby/gems/2.3.0/gems/turn-0.9.7/Index.rb
/usr/lib64/ruby/gems/2.3.0/gems/turn-0.9.7/LICENSE.txt
/usr/lib64/ruby/gems/2.3.0/gems/turn-0.9.7/NOTICE.md
/usr/lib64/ruby/gems/2.3.0/gems/turn-0.9.7/README.md
/usr/lib64/ruby/gems/2.3.0/gems/turn-0.9.7/Release.txt
/usr/lib64/ruby/gems/2.3.0/gems/turn-0.9.7/Version.txt
/usr/lib64/ruby/gems/2.3.0/gems/turn-0.9.7/bin/turn
/usr/lib64/ruby/gems/2.3.0/gems/turn-0.9.7/lib/turn.rb
/usr/lib64/ruby/gems/2.3.0/gems/turn-0.9.7/lib/turn/autoload.rb
/usr/lib64/ruby/gems/2.3.0/gems/turn-0.9.7/lib/turn/autorun.rb
/usr/lib64/ruby/gems/2.3.0/gems/turn-0.9.7/lib/turn/bin.rb
/usr/lib64/ruby/gems/2.3.0/gems/turn-0.9.7/lib/turn/colorize.rb
/usr/lib64/ruby/gems/2.3.0/gems/turn-0.9.7/lib/turn/command.rb
/usr/lib64/ruby/gems/2.3.0/gems/turn-0.9.7/lib/turn/components.rb
/usr/lib64/ruby/gems/2.3.0/gems/turn-0.9.7/lib/turn/components/case.rb
/usr/lib64/ruby/gems/2.3.0/gems/turn-0.9.7/lib/turn/components/method.rb
/usr/lib64/ruby/gems/2.3.0/gems/turn-0.9.7/lib/turn/components/suite.rb
/usr/lib64/ruby/gems/2.3.0/gems/turn-0.9.7/lib/turn/configuration.rb
/usr/lib64/ruby/gems/2.3.0/gems/turn-0.9.7/lib/turn/controller.rb
/usr/lib64/ruby/gems/2.3.0/gems/turn-0.9.7/lib/turn/core_ext.rb
/usr/lib64/ruby/gems/2.3.0/gems/turn-0.9.7/lib/turn/decorators/topten_decorator.rb
/usr/lib64/ruby/gems/2.3.0/gems/turn-0.9.7/lib/turn/minitest.rb
/usr/lib64/ruby/gems/2.3.0/gems/turn-0.9.7/lib/turn/reporter.rb
/usr/lib64/ruby/gems/2.3.0/gems/turn-0.9.7/lib/turn/reporters/cue_reporter.rb
/usr/lib64/ruby/gems/2.3.0/gems/turn-0.9.7/lib/turn/reporters/dot_reporter.rb
/usr/lib64/ruby/gems/2.3.0/gems/turn-0.9.7/lib/turn/reporters/marshal_reporter.rb
/usr/lib64/ruby/gems/2.3.0/gems/turn-0.9.7/lib/turn/reporters/outline_reporter.rb
/usr/lib64/ruby/gems/2.3.0/gems/turn-0.9.7/lib/turn/reporters/pretty_reporter.rb
/usr/lib64/ruby/gems/2.3.0/gems/turn-0.9.7/lib/turn/reporters/progress_reporter.rb
/usr/lib64/ruby/gems/2.3.0/gems/turn-0.9.7/lib/turn/runners/crossrunner.rb
/usr/lib64/ruby/gems/2.3.0/gems/turn-0.9.7/lib/turn/runners/isorunner.rb
/usr/lib64/ruby/gems/2.3.0/gems/turn-0.9.7/lib/turn/runners/loadrunner.rb
/usr/lib64/ruby/gems/2.3.0/gems/turn-0.9.7/lib/turn/runners/minirunner.rb
/usr/lib64/ruby/gems/2.3.0/gems/turn-0.9.7/lib/turn/runners/solorunner.rb
/usr/lib64/ruby/gems/2.3.0/gems/turn-0.9.7/lib/turn/runners/testrunner.rb
/usr/lib64/ruby/gems/2.3.0/gems/turn-0.9.7/lib/turn/testunit.rb
/usr/lib64/ruby/gems/2.3.0/gems/turn-0.9.7/lib/turn/version.rb
/usr/lib64/ruby/gems/2.3.0/gems/turn-0.9.7/test/helper.rb
/usr/lib64/ruby/gems/2.3.0/gems/turn-0.9.7/test/reporter_test.rb
/usr/lib64/ruby/gems/2.3.0/gems/turn-0.9.7/test/runner
/usr/lib64/ruby/gems/2.3.0/gems/turn-0.9.7/test/test_framework.rb
/usr/lib64/ruby/gems/2.3.0/gems/turn-0.9.7/test/test_reporters.rb
/usr/lib64/ruby/gems/2.3.0/gems/turn-0.9.7/test/test_runners.rb
/usr/lib64/ruby/gems/2.3.0/gems/turn-0.9.7/try/test_autorun_minitest.rb
/usr/lib64/ruby/gems/2.3.0/gems/turn-0.9.7/try/test_autorun_testunit.rb
/usr/lib64/ruby/gems/2.3.0/gems/turn-0.9.7/try/test_counts.rb
/usr/lib64/ruby/gems/2.3.0/gems/turn-0.9.7/try/test_sample.rb
/usr/lib64/ruby/gems/2.3.0/gems/turn-0.9.7/try/test_sample2.rb
/usr/lib64/ruby/gems/2.3.0/specifications/turn-0.9.7.gemspec

%files bin
%defattr(-,root,root,-)
/usr/bin/turn
