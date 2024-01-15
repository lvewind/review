<?php

use Dcat\Admin\Admin;
use Dcat\Admin\Grid;
use Dcat\Admin\Form;
use Dcat\Admin\Grid\Filter;
use Dcat\Admin\Show;

/**
 * Dcat-admin - admin builder based on Laravel.
 * @author jqh <https://github.com/jqhph>
 *
 * Bootstraper for Admin.
 *
 * Here you can remove builtin form field:
 *
 * extend custom field:
 * Dcat\Admin\Form::extend('php', PHPEditor::class);
 * Dcat\Admin\Grid\Column::extend('php', PHPEditor::class);
 * Dcat\Admin\Grid\Filter::extend('php', PHPEditor::class);
 *
 * Or require js and css assets:
 * Admin::css('/packages/prettydocs/css/styles.css');
 * Admin::js('/packages/prettydocs/js/main.js');
 *
 */

use Dcat\Admin\Layout\Menu;

Admin::menu(function (Menu $menu) {
    $menu->add([
        [
            'id'            => '81',
            'title'         => '巡检结果',
            'icon'          => 'fa-align-justify',
            'uri'           => 'inspection-result',
            'parent_id'     => 0,
        ],
        [
            'id'            => '82',
            'title'         => '巡检地点',
            'icon'          => 'fa-anchor',
            'uri'           => 'place',
            'parent_id'     => '0',
        ],
        [
            'id'            => '83',
            'title'         => '班次',
            'icon'          => 'fa-clock-o',
            'uri'           => 'scheduling',
            'parent_id'     => '0',
        ],
        [
            'id'            => '84',
            'title'         => '部门',
            'icon'          => 'fa-envira',
            'uri'           => 'department',
            'parent_id'     => '0',
        ],
        [
            'id'            => '85',
            'title'         => '巡检人',
            'icon'          => 'fa-user',
            'uri'           => 'inspector',
            'parent_id'     => '0',
        ],
    ]);
});
