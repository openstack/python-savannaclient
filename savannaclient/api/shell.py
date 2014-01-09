# Copyright 2013 Red Hat, Inc.
# All Rights Reserved.
#
#    Licensed under the Apache License, Version 2.0 (the "License"); you may
#    not use this file except in compliance with the License. You may obtain
#    a copy of the License at
#
#         http://www.apache.org/licenses/LICENSE-2.0
#
#    Unless required by applicable law or agreed to in writing, software
#    distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
#    WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
#    License for the specific language governing permissions and limitations
#    under the License.

from savannaclient.nova import utils


#
# Plugins
# ~~~~~~~
# plugins-list
#
# plugins-show --name <plugin> [--version <version>]
#

def do_plugins_list(cs, args):
    """Print a list of available plugins."""
    plugins = cs.plugins.list()
    columns = ('name', 'versions', 'title')
    utils.print_list(plugins, columns)


@utils.arg('--name',
           metavar='<plugin>',
           required=True,
           help='Name of plugin')
# TODO(mattf) - savannaclient does not support query w/ version
#@utils.arg('--version',
#           metavar='<version>',
#           help='Optional version')
def do_plugins_show(cs, args):
    """Show details of a plugin."""
    plugin = cs.plugins.get(args.name)
    utils.print_dict(plugin._info)


#
# Image Registry
# ~~~~~~~~~~~~~~
# image-list [--tag <tag>]*
#
# image-show --name <image>|--id <image_id>
#
# image-register --name <image>|--id <image_id>
#                [--username <name>] [--description <desc>]
#
# image-unregister --name <image>|--id <image_id>
#
# image-add-tag --name <image>|--id <image_id> --tag <tag>+
#
# image-remove-tag --name <image>|--id <image_id> --tag <tag>+
#

# TODO(mattf): [--tag <tag>]*
def do_image_list(cs, args):
    """Print a list of available plugins."""
    images = cs.images.list()
    columns = ('name', 'id', 'username', 'tags', 'description')
    utils.print_list(images, columns)


@utils.arg('--id',
           metavar='<image_id>',
           required=True,
           help='Id of image')
# TODO(mattf): --name <image>
def do_image_show(cs, args):
    """Show details of an image."""
    image = cs.images.get(args.id)
    utils.print_dict(image._info)


# TODO(mattf): Add --name
#@utils.arg('--name',
#           metavar='<image>',
#           required=True,
#           help='Name from Image index (e.g. glance index)')
@utils.arg('--id',
           metavar='<image_id>',
           required=True,
           help='Id from Image index (e.g. glance index)')
@utils.arg('--username',
           default='root',
           metavar='<name>',
           help='Username of privileged user in the image')
@utils.arg('--description',
           default='',
           metavar='<desc>',
           help='Description of image')
def do_image_register(cs, args):
    """Register an image from the Image index."""
    # TODO(mattf): image register should not be through update
    cs.images.update_image(args.id, args.username, args.description)
    # TODO(mattf): No indication of result, expect image details


# TODO(mattf): Add --name
#@utils.arg('--name',
#           metavar='<image>',
#           required=True,
#           help='Name from Image index (e.g. glance index)')
@utils.arg('--id',
           metavar='<image_id>',
           required=True,
           help='Image to unregister')
def do_image_unregister(cs, args):
    """Unregister an image."""
    cs.images.unregister_image(args.id)
    # TODO(mattf): No indication of result, expect result to display


# TODO(mattf): Add --name
#@utils.arg('--name',
#           metavar='<image>',
#           required=True,
#           help='Name from Image index (e.g. glance index)')
@utils.arg('--id',
           metavar='<image_id>',
           required=True,
           help='Image to tag')
# TODO(mattf): Change --tag to --tag+
@utils.arg('--tag',
           metavar='<tag>',
           required=True,
           help='Tag to add')
def do_image_add_tag(cs, args):
    """Add a tag to an image."""
    # TODO(mattf): Need proper add_tag API call
    cs.images.update_tags(args.id, cs.images.get(args.id).tags + [args.tag, ])
    # TODO(mattf): No indication of result, expect image details


# TODO(mattf): Add --name
#@utils.arg('--name',
#           metavar='<image>',
#           required=True,
#           help='Name from Image index (e.g. glance index)')
@utils.arg('--id',
           metavar='<image_id>',
           required=True,
           help='Image to tag')
# TODO(mattf): Change --tag to --tag+
@utils.arg('--tag',
           metavar='<tag>',
           required=True,
           help='Tag to add')
def do_image_remove_tag(cs, args):
    """Remove a tag from an image."""
    # TODO(mattf): Need proper remove_tag API call
    cs.images.update_tags(args.id,
                          filter(lambda x: x != args.tag,
                                 cs.images.get(args.id).tags))
    # TODO(mattf): No indication of result, expect image details