#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : rubygem-turn
Version  : 0.9.7
Release  : 2
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
/usr/lib64/ruby/gems/2.2.0/cache/turn-0.9.7.gem
/usr/lib64/ruby/gems/2.2.0/doc/turn-0.9.7/ri/MiniTest/cdesc-MiniTest.ri
/usr/lib64/ruby/gems/2.2.0/doc/turn-0.9.7/ri/Object/cdesc-Object.ri
/usr/lib64/ruby/gems/2.2.0/doc/turn-0.9.7/ri/Object/test_load-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/turn-0.9.7/ri/String/cdesc-String.ri
/usr/lib64/ruby/gems/2.2.0/doc/turn-0.9.7/ri/String/indent-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/turn-0.9.7/ri/String/tab-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/turn-0.9.7/ri/String/tabto-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/turn-0.9.7/ri/Test/Unit/Failure/cdesc-Failure.ri
/usr/lib64/ruby/gems/2.2.0/doc/turn-0.9.7/ri/Test/Unit/cdesc-Unit.ri
/usr/lib64/ruby/gems/2.2.0/doc/turn-0.9.7/ri/Test/cdesc-Test.ri
/usr/lib64/ruby/gems/2.2.0/doc/turn-0.9.7/ri/Turn/Colorize/blue-c.ri
/usr/lib64/ruby/gems/2.2.0/doc/turn-0.9.7/ri/Turn/Colorize/bold-c.ri
/usr/lib64/ruby/gems/2.2.0/doc/turn-0.9.7/ri/Turn/Colorize/cdesc-Colorize.ri
/usr/lib64/ruby/gems/2.2.0/doc/turn-0.9.7/ri/Turn/Colorize/color_supported%3f-c.ri
/usr/lib64/ruby/gems/2.2.0/doc/turn-0.9.7/ri/Turn/Colorize/colorize%3f-c.ri
/usr/lib64/ruby/gems/2.2.0/doc/turn-0.9.7/ri/Turn/Colorize/colorize%3f-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/turn-0.9.7/ri/Turn/Colorize/error-c.ri
/usr/lib64/ruby/gems/2.2.0/doc/turn-0.9.7/ri/Turn/Colorize/fail-c.ri
/usr/lib64/ruby/gems/2.2.0/doc/turn-0.9.7/ri/Turn/Colorize/green-c.ri
/usr/lib64/ruby/gems/2.2.0/doc/turn-0.9.7/ri/Turn/Colorize/included-c.ri
/usr/lib64/ruby/gems/2.2.0/doc/turn-0.9.7/ri/Turn/Colorize/magenta-c.ri
/usr/lib64/ruby/gems/2.2.0/doc/turn-0.9.7/ri/Turn/Colorize/mark-c.ri
/usr/lib64/ruby/gems/2.2.0/doc/turn-0.9.7/ri/Turn/Colorize/pass-c.ri
/usr/lib64/ruby/gems/2.2.0/doc/turn-0.9.7/ri/Turn/Colorize/red-c.ri
/usr/lib64/ruby/gems/2.2.0/doc/turn-0.9.7/ri/Turn/Colorize/skip-c.ri
/usr/lib64/ruby/gems/2.2.0/doc/turn-0.9.7/ri/Turn/Command/ansi-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/turn-0.9.7/ri/Turn/Command/cdesc-Command.ri
/usr/lib64/ruby/gems/2.2.0/doc/turn-0.9.7/ri/Turn/Command/decmode-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/turn-0.9.7/ri/Turn/Command/live-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/turn-0.9.7/ri/Turn/Command/loadpath-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/turn-0.9.7/ri/Turn/Command/log-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/turn-0.9.7/ri/Turn/Command/main-c.ri
/usr/lib64/ruby/gems/2.2.0/doc/turn-0.9.7/ri/Turn/Command/main-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/turn-0.9.7/ri/Turn/Command/mark-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/turn-0.9.7/ri/Turn/Command/matchcase-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/turn-0.9.7/ri/Turn/Command/natural-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/turn-0.9.7/ri/Turn/Command/new-c.ri
/usr/lib64/ruby/gems/2.2.0/doc/turn-0.9.7/ri/Turn/Command/option_parser-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/turn-0.9.7/ri/Turn/Command/outmode-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/turn-0.9.7/ri/Turn/Command/pattern-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/turn-0.9.7/ri/Turn/Command/requires-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/turn-0.9.7/ri/Turn/Command/runmode-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/turn-0.9.7/ri/Turn/Command/trace-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/turn-0.9.7/ri/Turn/Command/verbose-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/turn-0.9.7/ri/Turn/Configuration/ansi%3d-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/turn-0.9.7/ri/Turn/Configuration/ansi%3f-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/turn-0.9.7/ri/Turn/Configuration/cdesc-Configuration.ri
/usr/lib64/ruby/gems/2.2.0/doc/turn-0.9.7/ri/Turn/Configuration/decorate_reporter-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/turn-0.9.7/ri/Turn/Configuration/decorator_class-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/turn-0.9.7/ri/Turn/Configuration/environment_ansi-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/turn-0.9.7/ri/Turn/Configuration/environment_format-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/turn-0.9.7/ri/Turn/Configuration/environment_mode-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/turn-0.9.7/ri/Turn/Configuration/environment_trace-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/turn-0.9.7/ri/Turn/Configuration/exclude%3d-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/turn-0.9.7/ri/Turn/Configuration/exclude-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/turn-0.9.7/ri/Turn/Configuration/files-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/turn-0.9.7/ri/Turn/Configuration/format-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/turn-0.9.7/ri/Turn/Configuration/framework-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/turn-0.9.7/ri/Turn/Configuration/initialize_defaults-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/turn-0.9.7/ri/Turn/Configuration/list_option-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/turn-0.9.7/ri/Turn/Configuration/live%3f-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/turn-0.9.7/ri/Turn/Configuration/live-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/turn-0.9.7/ri/Turn/Configuration/loadpath%3d-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/turn-0.9.7/ri/Turn/Configuration/loadpath-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/turn-0.9.7/ri/Turn/Configuration/log-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/turn-0.9.7/ri/Turn/Configuration/mark-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/turn-0.9.7/ri/Turn/Configuration/matchcase-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/turn-0.9.7/ri/Turn/Configuration/mode-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/turn-0.9.7/ri/Turn/Configuration/natural%3f-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/turn-0.9.7/ri/Turn/Configuration/natural-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/turn-0.9.7/ri/Turn/Configuration/new-c.ri
/usr/lib64/ruby/gems/2.2.0/doc/turn-0.9.7/ri/Turn/Configuration/pattern-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/turn-0.9.7/ri/Turn/Configuration/reporter-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/turn-0.9.7/ri/Turn/Configuration/reporter_class-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/turn-0.9.7/ri/Turn/Configuration/reporter_options-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/turn-0.9.7/ri/Turn/Configuration/requires%3d-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/turn-0.9.7/ri/Turn/Configuration/requires-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/turn-0.9.7/ri/Turn/Configuration/runmode-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/turn-0.9.7/ri/Turn/Configuration/suite_name-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/turn-0.9.7/ri/Turn/Configuration/tests%3d-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/turn-0.9.7/ri/Turn/Configuration/tests-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/turn-0.9.7/ri/Turn/Configuration/trace-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/turn-0.9.7/ri/Turn/Configuration/verbose%3f-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/turn-0.9.7/ri/Turn/Configuration/verbose-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/turn-0.9.7/ri/Turn/Controller/cdesc-Controller.ri
/usr/lib64/ruby/gems/2.2.0/doc/turn-0.9.7/ri/Turn/Controller/config-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/turn-0.9.7/ri/Turn/Controller/new-c.ri
/usr/lib64/ruby/gems/2.2.0/doc/turn-0.9.7/ri/Turn/Controller/runner-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/turn-0.9.7/ri/Turn/Controller/setup-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/turn-0.9.7/ri/Turn/Controller/start-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/turn-0.9.7/ri/Turn/CrossRunner/cdesc-CrossRunner.ri
/usr/lib64/ruby/gems/2.2.0/doc/turn-0.9.7/ri/Turn/CrossRunner/start-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/turn-0.9.7/ri/Turn/CueReporter/cdesc-CueReporter.ri
/usr/lib64/ruby/gems/2.2.0/doc/turn-0.9.7/ri/Turn/CueReporter/error-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/turn-0.9.7/ri/Turn/CueReporter/fail-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/turn-0.9.7/ri/Turn/CueReporter/finish_suite-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/turn-0.9.7/ri/Turn/CueReporter/finish_test-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/turn-0.9.7/ri/Turn/CueReporter/pass-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/turn-0.9.7/ri/Turn/CueReporter/prompt-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/turn-0.9.7/ri/Turn/CueReporter/show_captured_output-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/turn-0.9.7/ri/Turn/CueReporter/show_captured_stderr-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/turn-0.9.7/ri/Turn/CueReporter/show_captured_stdout-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/turn-0.9.7/ri/Turn/CueReporter/skip-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/turn-0.9.7/ri/Turn/CueReporter/start_case-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/turn-0.9.7/ri/Turn/CueReporter/start_suite-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/turn-0.9.7/ri/Turn/CueReporter/start_test-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/turn-0.9.7/ri/Turn/DotReporter/cdesc-DotReporter.ri
/usr/lib64/ruby/gems/2.2.0/doc/turn-0.9.7/ri/Turn/DotReporter/error-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/turn-0.9.7/ri/Turn/DotReporter/fail-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/turn-0.9.7/ri/Turn/DotReporter/finish_case-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/turn-0.9.7/ri/Turn/DotReporter/finish_suite-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/turn-0.9.7/ri/Turn/DotReporter/finish_test-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/turn-0.9.7/ri/Turn/DotReporter/pass-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/turn-0.9.7/ri/Turn/DotReporter/skip-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/turn-0.9.7/ri/Turn/DotReporter/start_case-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/turn-0.9.7/ri/Turn/DotReporter/start_suite-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/turn-0.9.7/ri/Turn/DotReporter/start_test-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/turn-0.9.7/ri/Turn/IsoRunner/cdesc-IsoRunner.ri
/usr/lib64/ruby/gems/2.2.0/doc/turn-0.9.7/ri/Turn/IsoRunner/log_report-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/turn-0.9.7/ri/Turn/IsoRunner/new-c.ri
/usr/lib64/ruby/gems/2.2.0/doc/turn-0.9.7/ri/Turn/IsoRunner/reporter-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/turn-0.9.7/ri/Turn/IsoRunner/start-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/turn-0.9.7/ri/Turn/IsoRunner/test_loop_runner-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/turn-0.9.7/ri/Turn/MarshalReporter/cdesc-MarshalReporter.ri
/usr/lib64/ruby/gems/2.2.0/doc/turn-0.9.7/ri/Turn/MarshalReporter/finish_suite-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/turn-0.9.7/ri/Turn/MiniRunner/_run_suite-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/turn-0.9.7/ri/Turn/MiniRunner/_run_suites-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/turn-0.9.7/ri/Turn/MiniRunner/cdesc-MiniRunner.ri
/usr/lib64/ruby/gems/2.2.0/doc/turn-0.9.7/ri/Turn/MiniRunner/new-c.ri
/usr/lib64/ruby/gems/2.2.0/doc/turn-0.9.7/ri/Turn/MiniRunner/normalize_filter-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/turn-0.9.7/ri/Turn/MiniRunner/output-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/turn-0.9.7/ri/Turn/MiniRunner/puke-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/turn-0.9.7/ri/Turn/MiniRunner/start-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/turn-0.9.7/ri/Turn/MiniRunner/turn_reporter-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/turn-0.9.7/ri/Turn/OutlineReporter/cdesc-OutlineReporter.ri
/usr/lib64/ruby/gems/2.2.0/doc/turn-0.9.7/ri/Turn/OutlineReporter/error-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/turn-0.9.7/ri/Turn/OutlineReporter/fail-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/turn-0.9.7/ri/Turn/OutlineReporter/finish_suite-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/turn-0.9.7/ri/Turn/OutlineReporter/finish_test-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/turn-0.9.7/ri/Turn/OutlineReporter/pass-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/turn-0.9.7/ri/Turn/OutlineReporter/show_captured_output-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/turn-0.9.7/ri/Turn/OutlineReporter/show_captured_stdout-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/turn-0.9.7/ri/Turn/OutlineReporter/skip-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/turn-0.9.7/ri/Turn/OutlineReporter/start_case-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/turn-0.9.7/ri/Turn/OutlineReporter/start_suite-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/turn-0.9.7/ri/Turn/OutlineReporter/start_test-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/turn-0.9.7/ri/Turn/PrettyReporter/banner-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/turn-0.9.7/ri/Turn/PrettyReporter/cdesc-PrettyReporter.ri
/usr/lib64/ruby/gems/2.2.0/doc/turn-0.9.7/ri/Turn/PrettyReporter/colorize_count-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/turn-0.9.7/ri/Turn/PrettyReporter/error-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/turn-0.9.7/ri/Turn/PrettyReporter/fail-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/turn-0.9.7/ri/Turn/PrettyReporter/finish_case-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/turn-0.9.7/ri/Turn/PrettyReporter/finish_suite-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/turn-0.9.7/ri/Turn/PrettyReporter/pass-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/turn-0.9.7/ri/Turn/PrettyReporter/prettify-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/turn-0.9.7/ri/Turn/PrettyReporter/skip-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/turn-0.9.7/ri/Turn/PrettyReporter/start_case-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/turn-0.9.7/ri/Turn/PrettyReporter/start_suite-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/turn-0.9.7/ri/Turn/PrettyReporter/start_test-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/turn-0.9.7/ri/Turn/ProgressReporter/cdesc-ProgressReporter.ri
/usr/lib64/ruby/gems/2.2.0/doc/turn-0.9.7/ri/Turn/ProgressReporter/error-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/turn-0.9.7/ri/Turn/ProgressReporter/fail-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/turn-0.9.7/ri/Turn/ProgressReporter/finish_case-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/turn-0.9.7/ri/Turn/ProgressReporter/finish_suite-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/turn-0.9.7/ri/Turn/ProgressReporter/new-c.ri
/usr/lib64/ruby/gems/2.2.0/doc/turn-0.9.7/ri/Turn/ProgressReporter/paint_line-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/turn-0.9.7/ri/Turn/ProgressReporter/post_report-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/turn-0.9.7/ri/Turn/ProgressReporter/skip-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/turn-0.9.7/ri/Turn/ProgressReporter/start_case-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/turn-0.9.7/ri/Turn/ProgressReporter/start_suite-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/turn-0.9.7/ri/Turn/ProgressReporter/test_tally-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/turn-0.9.7/ri/Turn/Reporter/cdesc-Reporter.ri
/usr/lib64/ruby/gems/2.2.0/doc/turn-0.9.7/ri/Turn/Reporter/clean_backtrace-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/turn-0.9.7/ri/Turn/Reporter/error-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/turn-0.9.7/ri/Turn/Reporter/fail-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/turn-0.9.7/ri/Turn/Reporter/filter_backtrace-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/turn-0.9.7/ri/Turn/Reporter/finish_case-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/turn-0.9.7/ri/Turn/Reporter/finish_suite-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/turn-0.9.7/ri/Turn/Reporter/finish_test-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/turn-0.9.7/ri/Turn/Reporter/io-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/turn-0.9.7/ri/Turn/Reporter/limit_backtrace-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/turn-0.9.7/ri/Turn/Reporter/naturalized_name-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/turn-0.9.7/ri/Turn/Reporter/new-c.ri
/usr/lib64/ruby/gems/2.2.0/doc/turn-0.9.7/ri/Turn/Reporter/pass-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/turn-0.9.7/ri/Turn/Reporter/skip-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/turn-0.9.7/ri/Turn/Reporter/start_case-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/turn-0.9.7/ri/Turn/Reporter/start_suite-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/turn-0.9.7/ri/Turn/Reporter/start_test-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/turn-0.9.7/ri/Turn/Reporter/ticktock-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/turn-0.9.7/ri/Turn/SoloRunner/cdesc-SoloRunner.ri
/usr/lib64/ruby/gems/2.2.0/doc/turn-0.9.7/ri/Turn/TestCase/cdesc-TestCase.ri
/usr/lib64/ruby/gems/2.2.0/doc/turn-0.9.7/ri/Turn/TestCase/count_assertions-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/turn-0.9.7/ri/Turn/TestCase/count_errors-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/turn-0.9.7/ri/Turn/TestCase/count_failures-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/turn-0.9.7/ri/Turn/TestCase/count_passes-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/turn-0.9.7/ri/Turn/TestCase/count_skips-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/turn-0.9.7/ri/Turn/TestCase/count_tests-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/turn-0.9.7/ri/Turn/TestCase/counts-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/turn-0.9.7/ri/Turn/TestCase/each-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/turn-0.9.7/ri/Turn/TestCase/error%3f-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/turn-0.9.7/ri/Turn/TestCase/fail%3f-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/turn-0.9.7/ri/Turn/TestCase/files-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/turn-0.9.7/ri/Turn/TestCase/message-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/turn-0.9.7/ri/Turn/TestCase/name-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/turn-0.9.7/ri/Turn/TestCase/new-c.ri
/usr/lib64/ruby/gems/2.2.0/doc/turn-0.9.7/ri/Turn/TestCase/new_test-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/turn-0.9.7/ri/Turn/TestCase/pass%3f-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/turn-0.9.7/ri/Turn/TestCase/size-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/turn-0.9.7/ri/Turn/TestCase/tests-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/turn-0.9.7/ri/Turn/TestMethod/backtrace-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/turn-0.9.7/ri/Turn/TestMethod/cdesc-TestMethod.ri
/usr/lib64/ruby/gems/2.2.0/doc/turn-0.9.7/ri/Turn/TestMethod/error%21-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/turn-0.9.7/ri/Turn/TestMethod/error%3f-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/turn-0.9.7/ri/Turn/TestMethod/fail%21-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/turn-0.9.7/ri/Turn/TestMethod/fail%3f-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/turn-0.9.7/ri/Turn/TestMethod/file-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/turn-0.9.7/ri/Turn/TestMethod/message-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/turn-0.9.7/ri/Turn/TestMethod/name-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/turn-0.9.7/ri/Turn/TestMethod/new-c.ri
/usr/lib64/ruby/gems/2.2.0/doc/turn-0.9.7/ri/Turn/TestMethod/pass%3f-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/turn-0.9.7/ri/Turn/TestMethod/raised-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/turn-0.9.7/ri/Turn/TestMethod/skip%21-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/turn-0.9.7/ri/Turn/TestMethod/skip%3f-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/turn-0.9.7/ri/Turn/TestMethod/to_s-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/turn-0.9.7/ri/Turn/TestRunner/attach_to_mediator-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/turn-0.9.7/ri/Turn/TestRunner/cdesc-TestRunner.ri
/usr/lib64/ruby/gems/2.2.0/doc/turn-0.9.7/ri/Turn/TestRunner/new-c.ri
/usr/lib64/ruby/gems/2.2.0/doc/turn-0.9.7/ri/Turn/TestRunner/setup_mediator-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/turn-0.9.7/ri/Turn/TestRunner/t_attach_to_mediator-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/turn-0.9.7/ri/Turn/TestRunner/t_case_finished-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/turn-0.9.7/ri/Turn/TestRunner/t_case_started-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/turn-0.9.7/ri/Turn/TestRunner/t_fault-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/turn-0.9.7/ri/Turn/TestRunner/t_finished-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/turn-0.9.7/ri/Turn/TestRunner/t_started-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/turn-0.9.7/ri/Turn/TestRunner/t_test_finished-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/turn-0.9.7/ri/Turn/TestRunner/t_test_started-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/turn-0.9.7/ri/Turn/TestSuite/cases-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/turn-0.9.7/ri/Turn/TestSuite/cdesc-TestSuite.ri
/usr/lib64/ruby/gems/2.2.0/doc/turn-0.9.7/ri/Turn/TestSuite/count_assertions-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/turn-0.9.7/ri/Turn/TestSuite/count_errors-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/turn-0.9.7/ri/Turn/TestSuite/count_failures-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/turn-0.9.7/ri/Turn/TestSuite/count_passes-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/turn-0.9.7/ri/Turn/TestSuite/count_skips-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/turn-0.9.7/ri/Turn/TestSuite/count_tests-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/turn-0.9.7/ri/Turn/TestSuite/counts-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/turn-0.9.7/ri/Turn/TestSuite/each-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/turn-0.9.7/ri/Turn/TestSuite/name-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/turn-0.9.7/ri/Turn/TestSuite/new-c.ri
/usr/lib64/ruby/gems/2.2.0/doc/turn-0.9.7/ri/Turn/TestSuite/new_case-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/turn-0.9.7/ri/Turn/TestSuite/passed%3f-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/turn-0.9.7/ri/Turn/TestSuite/seed-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/turn-0.9.7/ri/Turn/TestSuite/size%3d-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/turn-0.9.7/ri/Turn/TestSuite/size-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/turn-0.9.7/ri/Turn/ToptenDecorator/cdesc-ToptenDecorator.ri
/usr/lib64/ruby/gems/2.2.0/doc/turn-0.9.7/ri/Turn/ToptenDecorator/finish_suite-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/turn-0.9.7/ri/Turn/ToptenDecorator/finish_test-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/turn-0.9.7/ri/Turn/ToptenDecorator/format_test_name-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/turn-0.9.7/ri/Turn/ToptenDecorator/format_time-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/turn-0.9.7/ri/Turn/ToptenDecorator/method_missing-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/turn-0.9.7/ri/Turn/ToptenDecorator/new-c.ri
/usr/lib64/ruby/gems/2.2.0/doc/turn-0.9.7/ri/Turn/ToptenDecorator/start_case-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/turn-0.9.7/ri/Turn/ToptenDecorator/start_test-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/turn-0.9.7/ri/Turn/ToptenDecorator/test_key-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/turn-0.9.7/ri/Turn/ToptenDecorator/test_time_data-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/turn-0.9.7/ri/Turn/ToptenDecorator/test_times-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/turn-0.9.7/ri/Turn/ToptenDecorator/top_ten_times-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/turn-0.9.7/ri/Turn/bootstrap_legacy-c.ri
/usr/lib64/ruby/gems/2.2.0/doc/turn-0.9.7/ri/Turn/cdesc-Turn.ri
/usr/lib64/ruby/gems/2.2.0/doc/turn-0.9.7/ri/Turn/config-c.ri
/usr/lib64/ruby/gems/2.2.0/doc/turn-0.9.7/ri/cache.ri
/usr/lib64/ruby/gems/2.2.0/doc/turn-0.9.7/ri/page-CONTRIBUTING_md.ri
/usr/lib64/ruby/gems/2.2.0/doc/turn-0.9.7/ri/page-History_txt.ri
/usr/lib64/ruby/gems/2.2.0/doc/turn-0.9.7/ri/page-LICENSE_txt.ri
/usr/lib64/ruby/gems/2.2.0/doc/turn-0.9.7/ri/page-NOTICE_md.ri
/usr/lib64/ruby/gems/2.2.0/doc/turn-0.9.7/ri/page-README_md.ri
/usr/lib64/ruby/gems/2.2.0/doc/turn-0.9.7/ri/page-Release_txt.ri
/usr/lib64/ruby/gems/2.2.0/doc/turn-0.9.7/ri/page-Version_txt.ri
/usr/lib64/ruby/gems/2.2.0/gems/turn-0.9.7/CONTRIBUTING.md
/usr/lib64/ruby/gems/2.2.0/gems/turn-0.9.7/History.txt
/usr/lib64/ruby/gems/2.2.0/gems/turn-0.9.7/Index.rb
/usr/lib64/ruby/gems/2.2.0/gems/turn-0.9.7/LICENSE.txt
/usr/lib64/ruby/gems/2.2.0/gems/turn-0.9.7/NOTICE.md
/usr/lib64/ruby/gems/2.2.0/gems/turn-0.9.7/README.md
/usr/lib64/ruby/gems/2.2.0/gems/turn-0.9.7/Release.txt
/usr/lib64/ruby/gems/2.2.0/gems/turn-0.9.7/Version.txt
/usr/lib64/ruby/gems/2.2.0/gems/turn-0.9.7/bin/turn
/usr/lib64/ruby/gems/2.2.0/gems/turn-0.9.7/lib/turn.rb
/usr/lib64/ruby/gems/2.2.0/gems/turn-0.9.7/lib/turn/autoload.rb
/usr/lib64/ruby/gems/2.2.0/gems/turn-0.9.7/lib/turn/autorun.rb
/usr/lib64/ruby/gems/2.2.0/gems/turn-0.9.7/lib/turn/bin.rb
/usr/lib64/ruby/gems/2.2.0/gems/turn-0.9.7/lib/turn/colorize.rb
/usr/lib64/ruby/gems/2.2.0/gems/turn-0.9.7/lib/turn/command.rb
/usr/lib64/ruby/gems/2.2.0/gems/turn-0.9.7/lib/turn/components.rb
/usr/lib64/ruby/gems/2.2.0/gems/turn-0.9.7/lib/turn/components/case.rb
/usr/lib64/ruby/gems/2.2.0/gems/turn-0.9.7/lib/turn/components/method.rb
/usr/lib64/ruby/gems/2.2.0/gems/turn-0.9.7/lib/turn/components/suite.rb
/usr/lib64/ruby/gems/2.2.0/gems/turn-0.9.7/lib/turn/configuration.rb
/usr/lib64/ruby/gems/2.2.0/gems/turn-0.9.7/lib/turn/controller.rb
/usr/lib64/ruby/gems/2.2.0/gems/turn-0.9.7/lib/turn/core_ext.rb
/usr/lib64/ruby/gems/2.2.0/gems/turn-0.9.7/lib/turn/decorators/topten_decorator.rb
/usr/lib64/ruby/gems/2.2.0/gems/turn-0.9.7/lib/turn/minitest.rb
/usr/lib64/ruby/gems/2.2.0/gems/turn-0.9.7/lib/turn/reporter.rb
/usr/lib64/ruby/gems/2.2.0/gems/turn-0.9.7/lib/turn/reporters/cue_reporter.rb
/usr/lib64/ruby/gems/2.2.0/gems/turn-0.9.7/lib/turn/reporters/dot_reporter.rb
/usr/lib64/ruby/gems/2.2.0/gems/turn-0.9.7/lib/turn/reporters/marshal_reporter.rb
/usr/lib64/ruby/gems/2.2.0/gems/turn-0.9.7/lib/turn/reporters/outline_reporter.rb
/usr/lib64/ruby/gems/2.2.0/gems/turn-0.9.7/lib/turn/reporters/pretty_reporter.rb
/usr/lib64/ruby/gems/2.2.0/gems/turn-0.9.7/lib/turn/reporters/progress_reporter.rb
/usr/lib64/ruby/gems/2.2.0/gems/turn-0.9.7/lib/turn/runners/crossrunner.rb
/usr/lib64/ruby/gems/2.2.0/gems/turn-0.9.7/lib/turn/runners/isorunner.rb
/usr/lib64/ruby/gems/2.2.0/gems/turn-0.9.7/lib/turn/runners/loadrunner.rb
/usr/lib64/ruby/gems/2.2.0/gems/turn-0.9.7/lib/turn/runners/minirunner.rb
/usr/lib64/ruby/gems/2.2.0/gems/turn-0.9.7/lib/turn/runners/solorunner.rb
/usr/lib64/ruby/gems/2.2.0/gems/turn-0.9.7/lib/turn/runners/testrunner.rb
/usr/lib64/ruby/gems/2.2.0/gems/turn-0.9.7/lib/turn/testunit.rb
/usr/lib64/ruby/gems/2.2.0/gems/turn-0.9.7/lib/turn/version.rb
/usr/lib64/ruby/gems/2.2.0/gems/turn-0.9.7/test/helper.rb
/usr/lib64/ruby/gems/2.2.0/gems/turn-0.9.7/test/reporter_test.rb
/usr/lib64/ruby/gems/2.2.0/gems/turn-0.9.7/test/runner
/usr/lib64/ruby/gems/2.2.0/gems/turn-0.9.7/test/test_framework.rb
/usr/lib64/ruby/gems/2.2.0/gems/turn-0.9.7/test/test_reporters.rb
/usr/lib64/ruby/gems/2.2.0/gems/turn-0.9.7/test/test_runners.rb
/usr/lib64/ruby/gems/2.2.0/gems/turn-0.9.7/try/test_autorun_minitest.rb
/usr/lib64/ruby/gems/2.2.0/gems/turn-0.9.7/try/test_autorun_testunit.rb
/usr/lib64/ruby/gems/2.2.0/gems/turn-0.9.7/try/test_counts.rb
/usr/lib64/ruby/gems/2.2.0/gems/turn-0.9.7/try/test_sample.rb
/usr/lib64/ruby/gems/2.2.0/gems/turn-0.9.7/try/test_sample2.rb
/usr/lib64/ruby/gems/2.2.0/specifications/turn-0.9.7.gemspec

%files bin
%defattr(-,root,root,-)
/usr/bin/turn
