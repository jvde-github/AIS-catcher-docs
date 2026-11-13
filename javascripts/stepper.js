// A .stepper holds .stepper-step blocks, each opening with an h2. With this script one
// step shows at a time in a window like the website's wizard: the guide's name
// (data-eyebrow) and the step's title on top with dots and a counter, Back / Next below.
// Without it, and in print, the steps read top to bottom. A link to a heading inside a
// step opens that step. Inside a .stepper-stage the window stands on the harbour photo.
(function () {
    function titleOf(step) {
        var h = step.querySelector('h2');
        if (!h) return '';
        var c = h.cloneNode(true);
        var a = c.querySelector('.headerlink');
        if (a) a.remove();
        return c.textContent.trim();
    }

    function button(cls, text) {
        var b = document.createElement('button');
        b.type = 'button';
        b.className = cls;
        if (text) b.textContent = text;
        return b;
    }

    function init(root) {
        var steps = Array.prototype.filter.call(root.children, function (el) {
            return el.classList.contains('stepper-step');
        });
        if (steps.length < 2) return;
        var titles = steps.map(titleOf);

        var head = document.createElement('div');
        head.className = 'stepper-head';
        var name = document.createElement('div');
        if (root.dataset.eyebrow) {
            var eyebrow = document.createElement('p');
            eyebrow.className = 'stepper-eyebrow';
            eyebrow.textContent = root.dataset.eyebrow;
            name.appendChild(eyebrow);
        }
        // the step's own h2 stays for links and screen readers; this is its visible copy
        var title = document.createElement('p');
        title.className = 'stepper-title';
        title.setAttribute('aria-hidden', 'true');
        name.appendChild(title);
        var progress = document.createElement('div');
        progress.className = 'stepper-progress';
        var count = document.createElement('p');
        count.className = 'stepper-count';
        count.setAttribute('aria-live', 'polite');
        var dots = document.createElement('div');
        dots.className = 'stepper-dots';
        steps.forEach(function (s, i) {
            var d = button('stepper-dot');
            d.setAttribute('aria-label', 'Step ' + (i + 1) + ': ' + titles[i]);
            d.addEventListener('click', function () { go(i, true); });
            dots.appendChild(d);
        });
        progress.appendChild(dots);
        progress.appendChild(count);
        head.appendChild(name);
        head.appendChild(progress);

        var foot = document.createElement('div');
        foot.className = 'stepper-foot';
        var back = button('stepper-back', 'Back');
        var next = button('stepper-next');
        foot.appendChild(back);
        foot.appendChild(next);

        root.insertBefore(head, steps[0]);
        root.appendChild(foot);
        root.classList.add('stepper--on');
        if (root.parentElement.classList.contains('stepper-stage'))
            root.parentElement.classList.add('stepper-stage--on');

        var cur = 0;
        function go(i, moved) {
            cur = Math.max(0, Math.min(steps.length - 1, i));
            steps.forEach(function (s, j) { s.hidden = j !== cur; });
            Array.prototype.forEach.call(dots.children, function (d, j) {
                d.classList.toggle('is-done', j < cur);
                d.classList.toggle('is-current', j === cur);
                if (j === cur) d.setAttribute('aria-current', 'step');
                else d.removeAttribute('aria-current');
            });
            count.textContent = 'Step ' + (cur + 1) + ' of ' + steps.length;
            title.textContent = titles[cur];
            back.hidden = cur === 0;
            next.hidden = cur === steps.length - 1;
            if (!next.hidden) next.textContent = 'Next: ' + titles[cur + 1];
            if (!moved) return;
            var h = steps[cur].querySelector('h2');
            if (h && h.id) history.replaceState(null, '', '#' + h.id);
            if (root.getBoundingClientRect().top < 0) root.scrollIntoView({ block: 'start' });
            if (h) {
                h.setAttribute('tabindex', '-1');
                h.focus({ preventScroll: true });
            }
        }
        back.addEventListener('click', function () { go(cur - 1, true); });
        next.addEventListener('click', function () { go(cur + 1, true); });

        function fromHash() {
            if (!location.hash) return false;
            var t = document.getElementById(decodeURIComponent(location.hash.slice(1)));
            if (!t) return false;
            for (var i = 0; i < steps.length; i++) {
                if (steps[i].contains(t)) {
                    go(i, false);
                    t.scrollIntoView();
                    return true;
                }
            }
            return false;
        }
        if (!fromHash()) go(0, false);
        window.addEventListener('hashchange', fromHash);
    }

    Array.prototype.forEach.call(document.querySelectorAll('.stepper'), init);
})();
