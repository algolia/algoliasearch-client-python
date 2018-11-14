# -*- coding: utf-8 -*-
"""
Copyright (c) 2013 Algolia
http://www.algolia.com/

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights lw1
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in
all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
THE SOFTWARE.
"""

from .helpers import AlgoliaException


class AccountClient:
    """
    The Account Client
    """

    @staticmethod
    def copy_index(source_index, destination_index, request_options=None):
        """
        Copies the source index into the destination index. It works
        even between different accounts.
        """
        try:
            destination_index.get_settings()
        except AlgoliaException:
            pass
        else:
            raise AlgoliaException(
                'Destination index already exists. Please delete it before copying index across applications.')

        responses = []

        # Transfer settings
        settings = source_index.get_settings()
        responses.append(destination_index.set_settings(settings))

        # Transfer synonyms
        synonyms = list(source_index.iter_synonyms())
        responses.append(destination_index.batch_synonyms(synonyms))

        # Transfer rules
        rules = list(source_index.iter_rules())
        responses.append(destination_index.batch_rules(rules))

        # Transfer objects
        responses = []
        batch = []
        batch_size = 1000
        count = 0
        for obj in source_index.browse_all():
            batch.append(obj)
            count += 1

            if count == batch_size:
                response = destination_index.save_objects(batch)
                responses.append(response)
                batch = []
                count = 0

        if batch:
            response = destination_index.save_objects(batch)
            responses.append(response)

        return responses
