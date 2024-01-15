<?php

namespace App\Admin\Controllers;

use App\Admin\Repositories\Scheduling;
use Dcat\Admin\Form;
use Dcat\Admin\Grid;
use Dcat\Admin\Show;
use Dcat\Admin\Http\Controllers\AdminController;

class SchedulingController extends AdminController
{
    /**
     * Make a grid builder.
     *
     * @return Grid
     */
    protected function grid()
    {
        return Grid::make(new Scheduling(), function (Grid $grid) {
            $grid->column('id')->sortable();
            $grid->column('name');
            $grid->column('time_start');
            $grid->column('time_end');
            $grid->column('created_at');
            $grid->column('updated_at')->sortable();

            $grid->filter(function (Grid\Filter $filter) {
                $filter->equal('id');

            });
        });
    }

    /**
     * Make a show builder.
     *
     * @param mixed $id
     *
     * @return Show
     */
    protected function detail($id)
    {
        return Show::make($id, new Scheduling(), function (Show $show) {
            $show->field('id');
            $show->field('name');
            $show->field('time_start');
            $show->field('time_end');
//            $show->field('created_at');
//            $show->field('updated_at');
        });
    }

    /**
     * Make a form builder.
     *
     * @return Form
     */
    protected function form()
    {
        return Form::make(new Scheduling(), function (Form $form) {
            $form->display('id');
            $form->text('name');
            $form->timeRange('time_start', 'time_end');

//            $form->display('created_at');
//            $form->display('updated_at');
        });
    }
}
