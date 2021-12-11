# -*- coding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
STOP_RENDERING = runtime.STOP_RENDERING
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1639255557.4574556
_enable_loop = True
_template_filename = 'themes/custom/templates/index.tmpl'
_template_uri = 'index.tmpl'
_source_encoding = 'utf-8'
_exports = ['extra_head', 'content', 'content_header']


def _mako_get_namespace(context, name):
    try:
        return context.namespaces[(__name__, name)]
    except KeyError:
        _mako_generate_namespaces(context)
        return context.namespaces[(__name__, name)]
def _mako_generate_namespaces(context):
    ns = runtime.TemplateNamespace('helper', context._clean_inheritance_tokens(), templateuri='index_helper.tmpl', callables=None,  calling_uri=_template_uri)
    context.namespaces[(__name__, 'helper')] = ns

    ns = runtime.TemplateNamespace('math', context._clean_inheritance_tokens(), templateuri='math_helper.tmpl', callables=None,  calling_uri=_template_uri)
    context.namespaces[(__name__, 'math')] = ns

    ns = runtime.TemplateNamespace('comments', context._clean_inheritance_tokens(), templateuri='comments_helper.tmpl', callables=None,  calling_uri=_template_uri)
    context.namespaces[(__name__, 'comments')] = ns

    ns = runtime.TemplateNamespace('pagination', context._clean_inheritance_tokens(), templateuri='pagination_helper.tmpl', callables=None,  calling_uri=_template_uri)
    context.namespaces[(__name__, 'pagination')] = ns

    ns = runtime.TemplateNamespace('archive_nav', context._clean_inheritance_tokens(), templateuri='archive_navigation_helper.tmpl', callables=None,  calling_uri=_template_uri)
    context.namespaces[(__name__, 'archive_nav')] = ns

    ns = runtime.TemplateNamespace('feeds_translations', context._clean_inheritance_tokens(), templateuri='feeds_translations_helper.tmpl', callables=None,  calling_uri=_template_uri)
    context.namespaces[(__name__, 'feeds_translations')] = ns

def _mako_inherit(template, context):
    _mako_generate_namespaces(context)
    return runtime._inherit_from(context, 'base.tmpl', _template_uri)
def render_body(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        _import_ns = {}
        _mako_get_namespace(context, 'archive_nav')._populate(_import_ns, ['*'])
        _mako_get_namespace(context, 'feeds_translations')._populate(_import_ns, ['*'])
        author_pages_generated = _import_ns.get('author_pages_generated', context.get('author_pages_generated', UNDEFINED))
        messages = _import_ns.get('messages', context.get('messages', UNDEFINED))
        math = _mako_get_namespace(context, 'math')
        page_links = _import_ns.get('page_links', context.get('page_links', UNDEFINED))
        nextlink = _import_ns.get('nextlink', context.get('nextlink', UNDEFINED))
        def extra_head():
            return render_extra_head(context._locals(__M_locals))
        date_format = _import_ns.get('date_format', context.get('date_format', UNDEFINED))
        site_has_comments = _import_ns.get('site_has_comments', context.get('site_has_comments', UNDEFINED))
        posts = _import_ns.get('posts', context.get('posts', UNDEFINED))
        prev_next_links_reversed = _import_ns.get('prev_next_links_reversed', context.get('prev_next_links_reversed', UNDEFINED))
        pagination = _mako_get_namespace(context, 'pagination')
        permalink = _import_ns.get('permalink', context.get('permalink', UNDEFINED))
        feeds_translations = _mako_get_namespace(context, 'feeds_translations')
        kind = _import_ns.get('kind', context.get('kind', UNDEFINED))
        current_page = _import_ns.get('current_page', context.get('current_page', UNDEFINED))
        comments = _mako_get_namespace(context, 'comments')
        parent = _import_ns.get('parent', context.get('parent', UNDEFINED))
        pagekind = _import_ns.get('pagekind', context.get('pagekind', UNDEFINED))
        _link = _import_ns.get('_link', context.get('_link', UNDEFINED))
        front_index_header = _import_ns.get('front_index_header', context.get('front_index_header', UNDEFINED))
        index_teasers = _import_ns.get('index_teasers', context.get('index_teasers', UNDEFINED))
        prevlink = _import_ns.get('prevlink', context.get('prevlink', UNDEFINED))
        def content_header():
            return render_content_header(context._locals(__M_locals))
        def content():
            return render_content(context._locals(__M_locals))
        index_file = _import_ns.get('index_file', context.get('index_file', UNDEFINED))
        __M_writer = context.writer()
        __M_writer('\n')
        __M_writer('\n')
        __M_writer('\n')
        __M_writer('\n')
        __M_writer('\n')
        __M_writer('\n')
        __M_writer('\n\n')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'extra_head'):
            context['self'].extra_head(**pageargs)
        

        __M_writer('\n\n')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'content'):
            context['self'].content(**pageargs)
        

        __M_writer('\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_extra_head(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        _import_ns = {}
        _mako_get_namespace(context, 'archive_nav')._populate(_import_ns, ['*'])
        _mako_get_namespace(context, 'feeds_translations')._populate(_import_ns, ['*'])
        def extra_head():
            return render_extra_head(context)
        permalink = _import_ns.get('permalink', context.get('permalink', UNDEFINED))
        index_file = _import_ns.get('index_file', context.get('index_file', UNDEFINED))
        math = _mako_get_namespace(context, 'math')
        parent = _import_ns.get('parent', context.get('parent', UNDEFINED))
        posts = _import_ns.get('posts', context.get('posts', UNDEFINED))
        __M_writer = context.writer()
        __M_writer('\n    ')
        __M_writer(str(parent.extra_head()))
        __M_writer('\n')
        if posts and (permalink == '/' or permalink == '/' + index_file):
            __M_writer('        <link rel="prefetch" href="')
            __M_writer(str(posts[0].permalink()))
            __M_writer('" type="text/html">\n')
        __M_writer('    ')
        __M_writer(str(math.math_styles_ifposts(posts)))
        __M_writer('\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_content(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        _import_ns = {}
        _mako_get_namespace(context, 'archive_nav')._populate(_import_ns, ['*'])
        _mako_get_namespace(context, 'feeds_translations')._populate(_import_ns, ['*'])
        author_pages_generated = _import_ns.get('author_pages_generated', context.get('author_pages_generated', UNDEFINED))
        messages = _import_ns.get('messages', context.get('messages', UNDEFINED))
        date_format = _import_ns.get('date_format', context.get('date_format', UNDEFINED))
        page_links = _import_ns.get('page_links', context.get('page_links', UNDEFINED))
        nextlink = _import_ns.get('nextlink', context.get('nextlink', UNDEFINED))
        math = _mako_get_namespace(context, 'math')
        site_has_comments = _import_ns.get('site_has_comments', context.get('site_has_comments', UNDEFINED))
        posts = _import_ns.get('posts', context.get('posts', UNDEFINED))
        prev_next_links_reversed = _import_ns.get('prev_next_links_reversed', context.get('prev_next_links_reversed', UNDEFINED))
        pagination = _mako_get_namespace(context, 'pagination')
        feeds_translations = _mako_get_namespace(context, 'feeds_translations')
        kind = _import_ns.get('kind', context.get('kind', UNDEFINED))
        current_page = _import_ns.get('current_page', context.get('current_page', UNDEFINED))
        comments = _mako_get_namespace(context, 'comments')
        pagekind = _import_ns.get('pagekind', context.get('pagekind', UNDEFINED))
        _link = _import_ns.get('_link', context.get('_link', UNDEFINED))
        front_index_header = _import_ns.get('front_index_header', context.get('front_index_header', UNDEFINED))
        index_teasers = _import_ns.get('index_teasers', context.get('index_teasers', UNDEFINED))
        prevlink = _import_ns.get('prevlink', context.get('prevlink', UNDEFINED))
        def content_header():
            return render_content_header(context)
        def content():
            return render_content(context)
        __M_writer = context.writer()
        __M_writer('\n')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'content_header'):
            context['self'].content_header(**pageargs)
        

        __M_writer('\n')
        if 'main_index' in pagekind:
            __M_writer('    ')
            __M_writer(str(front_index_header))
            __M_writer('\n')
        __M_writer('<div class="row">\n<div class="col-md-12 blog-main">\n<div class="postindex">\n')
        for post in posts:
            __M_writer('    <article class="h-entry post-')
            __M_writer(str(post.meta('type')))
            __M_writer('" itemscope="itemscope" itemtype="http://schema.org/Article">\n    <header>\n        <h1 class="p-name entry-title"><a href="')
            __M_writer(str(post.permalink()))
            __M_writer('" class="u-url">')
            __M_writer(filters.html_escape(str(post.title())))
            __M_writer('</a></h1>\n        <div class="metadata">\n            <p class="byline author vcard"><span class="byline-name fn" itemprop="author">\n')
            if author_pages_generated:
                __M_writer('                <a href="')
                __M_writer(str(_link('author', post.author())))
                __M_writer('">')
                __M_writer(filters.html_escape(str(post.author())))
                __M_writer('</a>\n')
            else:
                __M_writer('                ')
                __M_writer(filters.html_escape(str(post.author())))
                __M_writer('\n')
            __M_writer('            </span></p>\n            <p class="dateline">\n            <a href="')
            __M_writer(str(post.permalink()))
            __M_writer('" rel="bookmark">\n            <time class="published dt-published" datetime="')
            __M_writer(str(post.formatted_date('webiso')))
            __M_writer('" itemprop="datePublished" title="')
            __M_writer(filters.html_escape(str(post.formatted_date(date_format))))
            __M_writer('">')
            __M_writer(filters.html_escape(str(post.formatted_date(date_format))))
            __M_writer('</time>\n')
            if post.updated and post.updated != post.date:
                __M_writer('                <span class="updated"> (')
                __M_writer(str(messages("updated")))
                __M_writer('\n                    <time class="dt-updated" datetime="')
                __M_writer(str(post.formatted_updated('webiso')))
                __M_writer('" itemprop="dateUpdated" title="')
                __M_writer(filters.html_escape(str(post.formatted_updated(date_format))))
                __M_writer('">')
                __M_writer(filters.html_escape(str(post.formatted_updated(date_format))))
                __M_writer('</time>)</span>\n')
            __M_writer('            </a>\n            </p>\n')
            if not post.meta('nocomments') and site_has_comments:
                __M_writer('                <p class="commentline">')
                __M_writer(str(comments.comment_link(post.permalink(), post._base_path)))
                __M_writer('\n')
            __M_writer('        </div>\n    </header>\n')
            if index_teasers:
                __M_writer('    <div class="p-summary entry-summary">\n    ')
                __M_writer(str(post.text(teaser_only=True)))
                __M_writer('\n    </div>\n')
            else:
                __M_writer('    <div class="e-content entry-content">\n    ')
                __M_writer(str(post.text(teaser_only=False)))
                __M_writer('\n    </div>\n')
            __M_writer('    </article>\n')
        __M_writer('</div>\n</div>\n</div>\n')
        if page_links:
            __M_writer('    ')
            __M_writer(str(pagination.page_navigation(current_page, page_links, prevlink, nextlink, prev_next_links_reversed)))
            __M_writer('\n')
        __M_writer(str(comments.comment_link_script()))
        __M_writer('\n')
        __M_writer(str(math.math_scripts_ifposts(posts)))
        __M_writer('\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_content_header(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        _import_ns = {}
        _mako_get_namespace(context, 'archive_nav')._populate(_import_ns, ['*'])
        _mako_get_namespace(context, 'feeds_translations')._populate(_import_ns, ['*'])
        feeds_translations = _mako_get_namespace(context, 'feeds_translations')
        def content_header():
            return render_content_header(context)
        kind = _import_ns.get('kind', context.get('kind', UNDEFINED))
        __M_writer = context.writer()
        __M_writer('\n    ')
        __M_writer(str(feeds_translations.translation_link(kind)))
        __M_writer('\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"filename": "themes/custom/templates/index.tmpl", "uri": "index.tmpl", "source_encoding": "utf-8", "line_map": {"23": 2, "26": 3, "29": 4, "32": 5, "35": 6, "38": 7, "44": 0, "80": 2, "81": 3, "82": 4, "83": 5, "84": 6, "85": 7, "86": 8, "91": 16, "96": 73, "102": 10, "116": 10, "117": 11, "118": 11, "119": 12, "120": 13, "121": 13, "122": 13, "123": 15, "124": 15, "125": 15, "131": 18, "161": 18, "166": 21, "167": 22, "168": 23, "169": 23, "170": 23, "171": 25, "172": 28, "173": 29, "174": 29, "175": 29, "176": 31, "177": 31, "178": 31, "179": 31, "180": 34, "181": 35, "182": 35, "183": 35, "184": 35, "185": 35, "186": 36, "187": 37, "188": 37, "189": 37, "190": 39, "191": 41, "192": 41, "193": 42, "194": 42, "195": 42, "196": 42, "197": 42, "198": 42, "199": 43, "200": 44, "201": 44, "202": 44, "203": 45, "204": 45, "205": 45, "206": 45, "207": 45, "208": 45, "209": 47, "210": 49, "211": 50, "212": 50, "213": 50, "214": 52, "215": 54, "216": 55, "217": 56, "218": 56, "219": 58, "220": 59, "221": 60, "222": 60, "223": 63, "224": 65, "225": 68, "226": 69, "227": 69, "228": 69, "229": 71, "230": 71, "231": 72, "232": 72, "238": 19, "249": 19, "250": 20, "251": 20, "257": 251}}
__M_END_METADATA
"""
