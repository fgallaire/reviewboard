from django.utils import simplejson
                                 '%(github_public_repo_name)s/issues#issue/%%s',
    supports_bug_trackers = True
        except Exception, e:
                body=simplejson.dumps(body))
        except (urllib2.HTTPError, urllib2.URLError), e:
                rsp = simplejson.loads(data)
            return simplejson.loads(data)
        except (urllib2.URLError, urllib2.HTTPError), e:
                rsp = simplejson.loads(data)