<?php

namespace App\Admin\Controllers;

use App\Admin\Repositories\ProjectResult;
use Dcat\Admin\Form;
use Dcat\Admin\Grid;
use Dcat\Admin\Show;
use Dcat\Admin\Http\Controllers\AdminController;

class ProjectResultController extends AdminController
{
    /**
     * Make a grid builder.
     *
     * @return Grid
     */
    protected function grid()
    {
        return Grid::make(new ProjectResult(), function (Grid $grid) {
            $grid->column('id')->sortable();
            $grid->column('name');
            $grid->column('inspection_result_id');
            $grid->column('inspection_datetime');
            $grid->column('inspection_status');
            $grid->column('photo');
            $grid->column('video');
            $grid->column('note');
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
        return Show::make($id, new ProjectResult(), function (Show $show) {
            $show->field('id');
            $show->field('name');
            $show->field('inspection_result_id');
            $show->field('inspection_datetime');
            $show->field('inspection_status');
            $show->field('photo');
            $show->field('video');
            $show->field('note');
            $show->field('created_at');
            $show->field('updated_at');
        });
    }

    /**
     * Make a form builder.
     *
     * @return Form
     */
    protected function form()
    {
        return Form::make(new ProjectResult(), function (Form $form) {
            $form->display('id');
            $form->text('name');
            $form->text('inspection_result_id');
            $form->text('inspection_datetime');
            $form->text('inspection_status');
            $form->text('photo');
            $form->text('video');
            $form->text('note');
        
            $form->display('created_at');
            $form->display('updated_at');
        });
    }
}
