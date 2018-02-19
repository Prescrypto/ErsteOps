/*
 Highstock JS v2.1.3 (2015-02-27)

 (c) 2014 Highsoft AS
 Authors: Jon Arild Nygard / Oystein Moseng

 License: www.highcharts.com/license
*/
(function(f) {
  var i = f.seriesTypes,
    l = f.merge,
    t = f.extendClass,
    u = f.getOptions().plotOptions,
    v = function() {},
    m = f.each,
    s = f.pick,
    n = f.Series,
    q = f.Color;
  u.treemap = l(u.scatter, {
    showInLegend: !1,
    marker: !1,
    borderColor: '#E0E0E0',
    borderWidth: 1,
    dataLabels: {
      enabled: !0,
      defer: !1,
      verticalAlign: 'middle',
      formatter: function() {
        return this.point.name || this.point.id;
      },
      inside: !0,
    },
    tooltip: {
      headerFormat: '',
      pointFormat: '<b>{point.name}</b>: {point.value}</b><br/>',
    },
    layoutAlgorithm: 'sliceAndDice',
    layoutStartingDirection: 'vertical',
    alternateStartingDirection: !1,
    levelIsConstant: !0,
    states: {
      hover: {
        borderColor: '#A0A0A0',
        brightness: i.heatmap ? 0 : 0.1,
        shadow: !1,
      },
    },
    drillUpButton: { position: { align: 'left', x: 10, y: -50 } },
  });
  i.treemap = t(
    i.scatter,
    l(
      {
        pointAttrToOptions: {
          stroke: 'borderColor',
          'stroke-width': 'borderWidth',
          fill: 'color',
          dashstyle: 'borderDashStyle',
        },
        pointArrayMap: ['value'],
        axisTypes: i.heatmap
          ? ['xAxis', 'yAxis', 'colorAxis']
          : ['xAxis', 'yAxis'],
        optionalAxis: 'colorAxis',
        getSymbol: v,
        parallelArrays: ['x', 'y', 'value', 'colorValue'],
        colorKey: 'colorValue',
        translateColors: i.heatmap && i.heatmap.prototype.translateColors,
      },
      {
        type: 'treemap',
        trackerGroups: ['group', 'dataLabelsGroup'],
        pointClass: t(f.Point, {
          setState: function(a, b) {
            f.Point.prototype.setState.call(this, a, b);
            a === 'hover'
              ? this.dataLabel && this.dataLabel.attr({ zIndex: 1002 })
              : this.dataLabel &&
                this.dataLabel.attr({ zIndex: this.pointAttr[''].zIndex + 1 });
          },
        }),
        handleLayout: function() {
          var a = this.tree,
            b;
          if (this.points.length) {
            if (!a) (this.nodeMap = []), (a = this.tree = this.getTree());
            if (!this.rootNode) this.rootNode = '';
            this.levelMap = this.getLevels();
            m(this.points, function(a) {
              delete a.plotX;
              delete a.plotY;
            });
            b = this.getSeriesArea(a.val);
            this.nodeMap[''].values = b;
            this.calculateArea(a, b);
            this.setPointValues();
          }
        },
        getTree: function() {
          var a = this,
            b = 0,
            c = [],
            d = [],
            e,
            g = function(a) {
              m(c[a], function(a) {
                c[''].push(a);
              });
            },
            h = function(b, c, d, e, g, k) {
              var w = [],
                f = [],
                i = 0,
                l;
              l = g[c];
              var r, n, q;
              n = function() {
                var a = 0,
                  b = !1;
                f.length !== 0 &&
                  m(f, function(c) {
                    r.val > c.val && !b && (f.splice(a, 0, r), (b = !0));
                    a += 1;
                  });
                b || f.push(r);
              };
              l && (q = l.name || '');
              e[b] !== void 0 &&
                m(e[b], function(a) {
                  r = h(g[a].id, a, d + 1, e, g, b);
                  i += r.val;
                  n();
                  w.push(r);
                });
              l = s(g[c] && g[c].value, i, 0);
              c = {
                id: b,
                i: c,
                children: f,
                childrenTotal: i,
                val: l,
                level: d,
                parent: k,
                name: q,
              };
              return (a.nodeMap[c.id] = c);
            };
          m(this.points, function(a) {
            var e = '';
            d.push(a.id);
            if (a.parent !== void 0) e = a.parent;
            c[e] === void 0 && (c[e] = []);
            c[e].push(b);
            b += 1;
          });
          for (e in c)
            c.hasOwnProperty(e) &&
              e !== '' &&
              HighchartsAdapter.inArray(e, d) === -1 &&
              (g(e), delete c[e]);
          return h('', -1, 0, c, this.points, null);
        },
        calculateArea: function(a, b) {
          var c = [],
            d,
            e = this,
            g = e.options,
            h = g.layoutAlgorithm,
            f = g.alternateStartingDirection,
            i = this.nodeMap[this.rootNode].level,
            o = 0,
            j,
            p = g.levelIsConstant ? a.level : a.level - i,
            k;
          a.isVisible =
            a.id === this.rootNode ||
            !(!this.nodeMap[a.parent] || !this.nodeMap[a.parent].isVisible);
          p = p > 0 ? p : 0;
          if (this.levelMap[p + 1]) {
            j = this.levelMap[p + 1];
            if (j.layoutAlgorithm && e[j.layoutAlgorithm])
              h = j.layoutAlgorithm;
            if (j.layoutStartingDirection)
              b.direction = j.layoutStartingDirection === 'vertical' ? 0 : 1;
          }
          c = e[h](b, a.children);
          m(a.children, function(h) {
            p = g.levelIsConstant ? h.level : h.level - i;
            k = e.points[h.i];
            k.level = p;
            d = c[o];
            d.val = h.childrenTotal;
            d.direction = b.direction;
            if (f) d.direction = 1 - d.direction;
            h.values = d;
            h.isVisible = a.isVisible;
            k.node = h;
            k.value = h.val;
            k.isLeaf = !0;
            if (h.children.length) (k.isLeaf = !1), e.calculateArea(h, d);
            o += 1;
          });
        },
        setPointValues: function() {
          var a = this,
            b = a.xAxis,
            c = a.yAxis;
          a.nodeMap[''].values = { x: 0, y: 0, width: 100, height: 100 };
          m(a.points, function(d) {
            var e = d.node.values,
              g,
              h,
              f;
            e.x /= a.axisRatio;
            e.width /= a.axisRatio;
            g = Math.round(b.translate(e.x, 0, 0, 0, 1));
            h = Math.round(b.translate(e.x + e.width, 0, 0, 0, 1));
            f = Math.round(c.translate(e.y, 0, 0, 0, 1));
            e = Math.round(c.translate(e.y + e.height, 0, 0, 0, 1));
            if (d.value > 0)
              (d.shapeType = 'rect'),
                (d.shapeArgs = {
                  x: Math.min(g, h),
                  y: Math.min(f, e),
                  width: Math.abs(h - g),
                  height: Math.abs(e - f),
                }),
                (d.plotX = d.shapeArgs.x + d.shapeArgs.width / 2),
                (d.plotY = d.shapeArgs.y + d.shapeArgs.height / 2);
          });
        },
        getSeriesArea: function(a) {
          var b = this.options.layoutStartingDirection === 'vertical' ? 0 : 1;
          return {
            x: 0,
            y: 0,
            width: 100 * (this.axisRatio = this.xAxis.len / this.yAxis.len),
            height: 100,
            direction: b,
            val: a,
          };
        },
        getLevels: function() {
          var a = [],
            b = this.options.levels;
          b &&
            m(b, function(b) {
              b.level !== void 0 && (a[b.level] = b);
            });
          return a;
        },
        setColorRecursive: function(a, b) {
          var c = this,
            d,
            e;
          if (a) {
            d = c.points[a.i];
            e = c.levelMap[a.level];
            b = s(d && d.options.color, e && e.color, b);
            if (d) d.color = b;
            a.children.length &&
              m(a.children, function(a) {
                c.setColorRecursive(a, b);
              });
          }
        },
        alg_func_group: function(a, b, c, d) {
          this.height = a;
          this.width = b;
          this.plot = d;
          this.startDirection = this.direction = c;
          this.lH = this.nH = this.lW = this.nW = this.total = 0;
          this.elArr = [];
          this.lP = {
            total: 0,
            lH: 0,
            nH: 0,
            lW: 0,
            nW: 0,
            nR: 0,
            lR: 0,
            aspectRatio: function(a, b) {
              return Math.max(a / b, b / a);
            },
          };
          this.addElement = function(a) {
            this.lP.total = this.elArr[this.elArr.length - 1];
            this.total += a;
            this.direction === 0
              ? ((this.lW = this.nW),
                (this.lP.lH = this.lP.total / this.lW),
                (this.lP.lR = this.lP.aspectRatio(this.lW, this.lP.lH)),
                (this.nW = this.total / this.height),
                (this.lP.nH = this.lP.total / this.nW),
                (this.lP.nR = this.lP.aspectRatio(this.nW, this.lP.nH)))
              : ((this.lH = this.nH),
                (this.lP.lW = this.lP.total / this.lH),
                (this.lP.lR = this.lP.aspectRatio(this.lP.lW, this.lH)),
                (this.nH = this.total / this.width),
                (this.lP.nW = this.lP.total / this.nH),
                (this.lP.nR = this.lP.aspectRatio(this.lP.nW, this.nH)));
            this.elArr.push(a);
          };
          this.reset = function() {
            this.lW = this.nW = 0;
            this.elArr = [];
            this.total = 0;
          };
        },
        alg_func_calcPoints: function(a, b, c, d) {
          var e,
            g,
            h,
            f,
            i = c.lW,
            o = c.lH,
            j = c.plot,
            p,
            k = 0,
            l = c.elArr.length - 1;
          b ? ((i = c.nW), (o = c.nH)) : (p = c.elArr[c.elArr.length - 1]);
          m(c.elArr, function(a) {
            if (b || k < l)
              c.direction === 0
                ? ((e = j.x), (g = j.y), (h = i), (f = a / h))
                : ((e = j.x), (g = j.y), (f = o), (h = a / f)),
                d.push({ x: e, y: g, width: h, height: f }),
                c.direction === 0 ? (j.y += f) : (j.x += h);
            k += 1;
          });
          c.reset();
          c.direction === 0 ? (c.width -= i) : (c.height -= o);
          j.y = j.parent.y + (j.parent.height - c.height);
          j.x = j.parent.x + (j.parent.width - c.width);
          if (a) c.direction = 1 - c.direction;
          b || c.addElement(p);
        },
        alg_func_lowAspectRatio: function(a, b, c) {
          var d = [],
            e = this,
            g,
            h = { x: b.x, y: b.y, parent: b },
            f = 0,
            i = c.length - 1,
            o = new this.alg_func_group(b.height, b.width, b.direction, h);
          m(c, function(c) {
            g = b.width * b.height * (c.val / b.val);
            o.addElement(g);
            o.lP.nR > o.lP.lR && e.alg_func_calcPoints(a, !1, o, d, h);
            f === i && e.alg_func_calcPoints(a, !0, o, d, h);
            f += 1;
          });
          return d;
        },
        alg_func_fill: function(a, b, c) {
          var d = [],
            e,
            g = b.direction,
            h = b.x,
            f = b.y,
            i = b.width,
            o = b.height,
            j,
            l,
            k,
            n;
          m(c, function(c) {
            e = b.width * b.height * (c.val / b.val);
            j = h;
            l = f;
            g === 0
              ? ((n = o), (k = e / n), (i -= k), (h += k))
              : ((k = i), (n = e / k), (o -= n), (f += n));
            d.push({ x: j, y: l, width: k, height: n });
            a && (g = 1 - g);
          });
          return d;
        },
        strip: function(a, b) {
          return this.alg_func_lowAspectRatio(!1, a, b);
        },
        squarified: function(a, b) {
          return this.alg_func_lowAspectRatio(!0, a, b);
        },
        sliceAndDice: function(a, b) {
          return this.alg_func_fill(!0, a, b);
        },
        stripes: function(a, b) {
          return this.alg_func_fill(!1, a, b);
        },
        translate: function() {
          n.prototype.translate.call(this);
          this.handleLayout();
          this.colorAxis
            ? this.translateColors()
            : this.options.colorByPoint ||
              this.setColorRecursive(this.tree, void 0);
        },
        drawDataLabels: function() {
          var a = this,
            b,
            c,
            d = this.dataLabelsGroup,
            e;
          m(a.points, function(d) {
            if (d.node.isVisible)
              if (((c = a.levelMap[d.level]), !d.isLeaf || c)) {
                b = void 0;
                d.isLeaf || (b = { enabled: !1 });
                if (c && (e = c.dataLabels))
                  (b = l(b, e)), (a._hasPointLabels = !0);
                b = l(b, d.options.dataLabels);
                d.dlOptions = b;
              } else delete d.dlOptions;
          });
          this.dataLabelsGroup = this.group;
          n.prototype.drawDataLabels.call(this);
          this.dataLabelsGroup = d;
        },
        alignDataLabel: i.column.prototype.alignDataLabel,
        drawPoints: function() {
          var a = this,
            b = a.points,
            c = a.options,
            d,
            e,
            g;
          m(b, function(b) {
            if (b.node.isVisible) {
              g = a.levelMap[b.level];
              d = {
                stroke: c.borderColor,
                'stroke-width': c.borderWidth,
                dashstyle: c.borderDashStyle,
                r: 0,
                fill: s(b.color, a.color),
              };
              if (g)
                (d.stroke = g.borderColor || d.stroke),
                  (d['stroke-width'] = g.borderWidth || d['stroke-width']),
                  (d.dashstyle = g.borderDashStyle || d.dashstyle);
              d.stroke = b.borderColor || d.stroke;
              d['stroke-width'] = b.borderWidth || d['stroke-width'];
              d.dashstyle = b.borderDashStyle || d.dashstyle;
              d.zIndex = 1e3 - b.level * 2;
              b.pointAttr = l(b.pointAttr);
              e = b.pointAttr.hover;
              e.zIndex = 1001;
              e.fill = q(d.fill)
                .brighten(c.states.hover.brightness)
                .get();
              if (!b.isLeaf)
                s(c.interactByLeaf, !c.allowDrillToNode)
                  ? ((d.fill = 'none'), delete e.fill)
                  : ((d.fill = q(d.fill)
                      .setOpacity(0.15)
                      .get()),
                    (e.fill = q(e.fill)
                      .setOpacity(0.75)
                      .get()));
              if (b.node.level <= a.nodeMap[a.rootNode].level)
                (d.fill = 'none'), (d.zIndex = 0), delete e.fill;
              b.pointAttr[''] = f.extend(b.pointAttr[''], d);
              b.dataLabel &&
                b.dataLabel.attr({ zIndex: b.pointAttr[''].zIndex + 1 });
            }
          });
          i.column.prototype.drawPoints.call(this);
          m(b, function(a) {
            a.graphic && a.graphic.attr(a.pointAttr['']);
          });
          c.allowDrillToNode && a.drillTo();
        },
        drillTo: function() {
          var a = this;
          m(a.points, function(b) {
            var c, d;
            if (
              b.node.isVisible &&
              (f.removeEvent(b, 'click'),
              b.graphic && b.graphic.css({ cursor: 'default' }),
              (c = a.options.interactByLeaf
                ? a.drillToByLeaf(b)
                : a.drillToByGroup(b)))
            )
              (d = a.nodeMap[a.rootNode].name || a.rootNode),
                b.graphic && b.graphic.css({ cursor: 'pointer' }),
                f.addEvent(b, 'click', function() {
                  b.setState('');
                  a.drillToNode(c);
                  a.showDrillUpButton(d);
                });
          });
        },
        drillToByGroup: function(a) {
          var b = !1;
          if (
            a.node.level - this.nodeMap[this.rootNode].level === 1 &&
            !a.isLeaf
          )
            b = a.id;
          return b;
        },
        drillToByLeaf: function(a) {
          var b = !1;
          if (a.node.parent !== this.rootNode && a.isLeaf)
            for (a = a.node; !b; )
              if (((a = this.nodeMap[a.parent]), a.parent === this.rootNode))
                b = a.id;
          return b;
        },
        drillUp: function() {
          var a = null;
          this.rootNode &&
            ((a = this.nodeMap[this.rootNode]),
            (a =
              a.parent !== null ? this.nodeMap[a.parent] : this.nodeMap['']));
          if (a !== null)
            this.drillToNode(a.id),
              a.id === ''
                ? (this.drillUpButton = this.drillUpButton.destroy())
                : ((a = this.nodeMap[a.parent]),
                  this.showDrillUpButton(a.name || a.id));
        },
        drillToNode: function(a) {
          var b = this.nodeMap[a].values;
          this.rootNode = a;
          this.xAxis.setExtremes(b.x, b.x + b.width, !1);
          this.yAxis.setExtremes(b.y, b.y + b.height, !1);
          this.chart.redraw();
        },
        showDrillUpButton: function(a) {
          var b = this,
            a = a || '< Back',
            c = b.options.drillUpButton,
            d,
            e;
          if (c.text) a = c.text;
          this.drillUpButton
            ? this.drillUpButton.attr({ text: a }).align()
            : ((e = (d = c.theme) && d.states),
              (this.drillUpButton = this.chart.renderer
                .button(
                  a,
                  null,
                  null,
                  function() {
                    b.drillUp();
                  },
                  d,
                  e && e.hover,
                  e && e.select
                )
                .attr({ align: c.position.align, zIndex: 9 })
                .add()
                .align(c.position, !1, c.relativeTo || 'plotBox')));
        },
        buildKDTree: v,
        drawLegendSymbol: f.LegendSymbolMixin.drawRectangle,
        getExtremes: function() {
          n.prototype.getExtremes.call(this, this.colorValueData);
          this.valueMin = this.dataMin;
          this.valueMax = this.dataMax;
          n.prototype.getExtremes.call(this);
        },
        bindAxes: function() {
          var a = {
            endOnTick: !1,
            gridLineWidth: 0,
            lineWidth: 0,
            min: 0,
            dataMin: 0,
            minPadding: 0,
            max: 100,
            dataMax: 100,
            maxPadding: 0,
            startOnTick: !1,
            title: null,
            tickPositions: [],
          };
          n.prototype.bindAxes.call(this);
          f.extend(this.yAxis.options, a);
          f.extend(this.xAxis.options, a);
        },
      }
    )
  );
})(Highcharts);
