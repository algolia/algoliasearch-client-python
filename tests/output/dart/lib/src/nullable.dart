import 'package:algolia_test/algolia_test.dart';

T empty<T>() =>
    switch (T) { String => '', Map => {}, _ => throw SkipException() } as T;
