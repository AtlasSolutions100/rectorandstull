/* Rector & Stull — site behaviour. No tracking, no third-party scripts. */
(function () {
  'use strict';

  /* Mobile menu */
  var toggle = document.querySelector('.menu-toggle');
  var nav = document.getElementById('primary-nav');
  if (toggle && nav) {
    var setOpen = function (open) {
      toggle.setAttribute('aria-expanded', String(open));
      nav.classList.toggle('is-open', open);
      toggle.textContent = open ? 'Close' : 'Menu';
    };
    toggle.addEventListener('click', function () {
      setOpen(toggle.getAttribute('aria-expanded') !== 'true');
    });
    nav.addEventListener('click', function (e) {
      if (e.target.closest('a')) setOpen(false);
    });
    document.addEventListener('keydown', function (e) {
      if (e.key === 'Escape' && toggle.getAttribute('aria-expanded') === 'true') {
        setOpen(false);
        toggle.focus();
      }
    });
  }

  /* Forms
     No backend yet. Each form carries:
       data-mailto   — destination address (TBD: hello@rectorandstull.com until the domain is bought)
       data-subject  — email subject
       data-endpoint — leave empty for now; set to a form-service URL later and the
                       same fields are POSTed as FormData instead of opening the mail app. */
  function labelFor(form, input) {
    var l = form.querySelector('label[for="' + input.id + '"]');
    return l ? l.childNodes[0].textContent.trim() : input.name;
  }

  function validate(form) {
    var firstBad = null;
    Array.prototype.forEach.call(form.elements, function (el) {
      if (!el.willValidate || el.type === 'submit') return;
      var ok = el.checkValidity();
      el.setAttribute('aria-invalid', ok ? 'false' : 'true');
      if (!ok && !firstBad) firstBad = el;
    });
    return firstBad;
  }

  function buildBody(form) {
    var lines = [];
    Array.prototype.forEach.call(form.elements, function (el) {
      if (!el.name || el.type === 'submit') return;
      var v = (el.value || '').trim();
      if (!v) return;
      lines.push(labelFor(form, el) + ': ' + v);
    });
    return lines.join('\n');
  }

  function handle(form) {
    var status = form.querySelector('.form-status');
    form.addEventListener('submit', function (e) {
      e.preventDefault();
      var bad = validate(form);
      if (bad) {
        status.textContent = 'Please check "' + labelFor(form, bad) + '": ' + bad.validationMessage;
        bad.focus();
        return;
      }
      /* Google Form backend: every submission lands in the "Rector & Stull website sign-ups" form (Responses tab). */
      var GFORM = 'https://docs.google.com/forms/d/e/1FAIpQLScFJV-zmDcRUPgGNVMfZYP5o58nS7sS_einK8gpbDji6HN6jg/formResponse';
      var ENTRY = { source: 'entry.181535244', name: 'entry.830234632', email: 'entry.1903066949', company: 'entry.1012657749', need: 'entry.548666740', message: 'entry.1587210976' };
      var body = new URLSearchParams();
      body.append(ENTRY.source, form.getAttribute('data-source') || form.id);
      Array.prototype.forEach.call(form.elements, function (el) {
        if (el.name && ENTRY[el.name]) body.append(ENTRY[el.name], (el.value || '').trim());
      });
      var btn = form.querySelector('button[type=submit]');
      if (btn) btn.disabled = true;
      status.textContent = 'Sending…';
      fetch(GFORM, { method: 'POST', mode: 'no-cors', body: body })
        .then(function () {
          form.reset();
          status.textContent = form.getAttribute('data-thanks') || 'Thank you. We received your message.';
        })
        .catch(function () {
          status.textContent = 'That did not go through. Please email us at ' + form.getAttribute('data-mailto') + '.';
        })
        .then(function () { if (btn) btn.disabled = false; });
      return;
      var endpoint = form.getAttribute('data-endpoint');
      if (endpoint) {
        status.textContent = 'Sending…';
        fetch(endpoint, { method: 'POST', body: new FormData(form), headers: { Accept: 'application/json' } })
          .then(function (r) {
            if (!r.ok) throw new Error(r.status);
            form.reset();
            status.textContent = 'Thanks. We got it and will reply soon.';
          })
          .catch(function () {
            status.textContent = 'Something went wrong. Please email us directly at ' + form.getAttribute('data-mailto') + '.';
          });
        return;
      }
      var to = form.getAttribute('data-mailto');
      var href = 'mailto:' + to +
        '?subject=' + encodeURIComponent(form.getAttribute('data-subject') || 'Hello') +
        '&body=' + encodeURIComponent(buildBody(form));
      window.location.href = href;
      status.innerHTML = '';
      status.appendChild(document.createTextNode('Your email app should open with the message ready to send. If it doesn’t, write to '));
      var a = document.createElement('a');
      a.href = 'mailto:' + to;
      a.textContent = to;
      status.appendChild(a);
      status.appendChild(document.createTextNode('.'));
    });
  }

  Array.prototype.forEach.call(document.querySelectorAll('form[data-mailto]'), handle);
})();
