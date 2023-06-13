package com.algolia.codegen.cts;

import com.samskivert.mustache.Mustache;
import com.samskivert.mustache.Template;
import java.io.IOException;
import java.io.Writer;
import java.util.Arrays;
import java.util.List;

// TODO: make escaing reserved words work with all languages.
public class EscapeDartLambda implements Mustache.Lambda {

  final List<String> reservedWords = Arrays.asList(
    "abstract",
    "as",
    "assert",
    "async",
    "await",
    "break",
    "case",
    "catch",
    "class",
    "const",
    "continue",
    "covariant",
    "default",
    "deferred",
    "do",
    "dynamic",
    "else",
    "enum",
    "export",
    "extends",
    "extension",
    "external",
    "factory",
    "false",
    "final",
    "finally",
    "for",
    "Function",
    "get",
    "hide",
    "if",
    "implements",
    "import",
    "in",
    "inout",
    "interface",
    "is",
    "late",
    "library",
    "mixin",
    "native",
    "new",
    "null",
    "of",
    "on",
    "operator",
    "out",
    "part",
    "patch",
    "required",
    "rethrow",
    "return",
    "set",
    "show",
    "source",
    "static",
    "super",
    "switch",
    "sync",
    "this",
    "throw",
    "true",
    "try",
    "typedef",
    "var",
    "void",
    "while",
    "with",
    "yield"
  );

  @Override
  public void execute(Template.Fragment fragment, Writer writer) throws IOException {
    String text = fragment.execute();
    writer.write(reservedWords.contains(text) ? text + "_" : text);
  }
}
